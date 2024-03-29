#!/usr/bin/env python3
from typing import List, Tuple
from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

class HLD:
    def __init__(self, N, G, root: int = 0):
        self.N = N                  # ノード数
        self.G = G                  # グラフ(隣接リスト)
        self.root = root            # 根
        self.depth_of_node = [0] * self.N                 # 各ノードの根からの距離(深さ)
        self.next_heavy_nodes = [-1] * self.N             # next_heavy_nodes[i] := heavy-pathにおいてノードiの次ノード番号 (0-indexed)
        self.parent_nodes = [None] * self.N               # parent_nodes[i] := ノードiの親ノード番号 (0-indexed)
        self.partial_tree_size = [None] * self.N          # partial_tree_size[i] := ノードi以下の部分木のサイズ

        self.heavy_paths = []                            # 全heavy_pathのリスト
        self.depth_of_heavy_path = []                    # depth_of_heavy_path[i] := i番目のheavy_pathの深さ(幾つのheavy_pathを乗り継いで到達するか)
        # Depth 0: [0] -------------------- [2] - [5] - [6] - [8]
        #           |                        |     |
        # Depth 1: [1] - [3] - [9] - [10]   [4]   [7] 
        #                       |
        # Depth 2:             [11]
        self.to_heavy_path_index = [0] * N               # ノードiはどのheavy_pathに所属するか(heavy_pathsのインデックス)
        self.indices_in_heavy_path = [0] * N             # ノードiがその属するheavy-pathの何番目にあたるのか。
        self.heads = [None] * self.N                     # ノードiが属するheavy-pathの先頭のノード番号
        self.ord = [None] * self.N                       # heavy-pathに割り当てた連続する番号
        # 上の例において
        # [0] -------------------- [5] - [6] - [7] - [8]
        #  |                        |     |
        # [1] - [2] - [3] - [4]    [10]  [11] 
        #              |
        #             [9]
        self.ord_to_node = [None] * N

    def path_query_range(self, a: int, b: int) -> List[Tuple[int, int]]:
        """
        ノードaとノードbの間に含まれるordの範囲[l, r)のリストを返す。
        """
        ret = []
        while True:
            if self.ord[a] > self.ord[b]:
                a, b = b, a
            if self.heads[a] == self.heads[b]:
                ret.append((self.ord[a], self.ord[b] + 1))
                return ret
            ret.append((self.ord[self.heads[b]], self.ord[b] + 1))
            b = self.parent_nodes[self.heads[b]]

    def subtree_query_range(self, a: int) -> Tuple[int, int]:
        """
        ノードaの部分木に含まれるordの範囲[l, r)のリストを返す。
        
        return [l, r) range that cover vertices of subtree v"""
        return (self.ord[a], self.ord[a] + self.partial_tree_size[a])

    def lca(self, u, v):
        while True:
            if self.ord[u] > self.ord[v]:
                u, v = v, u
            if self.heads[u] == self.heads[v]:
                return u
            v = self.parent_nodes[self.heads[v]]

    def _dfs(self, cur, depth):
        self.depth_of_node[cur] = depth
        sub_node_count = 1              # そのノード(を含む)配下の子ノード数
        heavy_path = None               # そのノードからのheavy-path
        max_heavy_path_length = 0       # 最大のheavy-path長
        for next in self.G[cur]:
            if self.parent_nodes[cur] == next:
                continue
            self.parent_nodes[next] = cur
            sub_node_total_count = self._dfs(next, depth + 1)
            # より長いパスが見つかったなら
            # heavy-pathとしてその子ノードの番号を仮置きする。
            if max_heavy_path_length < sub_node_total_count:
                heavy_path = next
                max_heavy_path_length = sub_node_total_count
            sub_node_count += sub_node_total_count
        self.partial_tree_size[cur] = sub_node_count
        self.next_heavy_nodes[cur] = heavy_path
        return sub_node_count

    def build(self):
        """
        グラフGをheavy-pathに沿って縮約
        """
        self._dfs(self.root, 0)
        stack = deque([(0, 0)])
        order = 0
        # DFS
        while stack:
            cur, depth_of_cur_heaby_path = stack.pop()
            head_of_heavy_path = cur
            cur_heavy_path = []
            k = len(self.heavy_paths)
            while cur is not None:
                self.ord[cur] = order
                self.ord_to_node[order] = cur
                self.heads[cur] = head_of_heavy_path
                self.indices_in_heavy_path[cur] = len(cur_heavy_path)
                cur_heavy_path.append(cur)
                self.to_heavy_path_index[cur] = k
                next_heavy_node = self.next_heavy_nodes[cur]

                # heavy-path以外をキューに入れておき、heavy-path上の次のノードの処理へ。
                for next in self.G[cur]:
                    if self.parent_nodes[cur] == next or next_heavy_node == next:
                        continue
                    stack.append((next, depth_of_cur_heaby_path + 1))
                cur = next_heavy_node
                order += 1
                
            self.heavy_paths.append(cur_heavy_path)
            self.depth_of_heavy_path.append(depth_of_cur_heaby_path)

class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (self.N + 1) # 1-indexedのため
        
    def add(self, pos, val):
        '''Add
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            A[pos] += val 
        '''
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] += val
            i += i & -i

    def deleteNonNegative(self, pos, val) -> int:
        '''Add
            O(logN)
            ※ multisetで使用される関数
            posは0-index。内部で1-indexedに変換される。
            すでにMultiSetに含まれている個数以上は削除されない。
            A[pos] -= val 
        '''
        actualSubstractVal = min(val, self.sum(pos) - self.sum(pos - 1)) # pos - 1は負になってもself.sum()は大丈夫
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] -= actualSubstractVal
            i += i & -i
        return actualSubstractVal

    def sum(self, pos):
        ''' Sum
            0からposまでの和を返す(posを含む)
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            Return Sum(A[0], ... , A[pos])
            posに負の値を指定されるとSum()すなわち0を返すのでマイナスの特段の考慮不要。
        '''
        res = 0
        i = pos + 1 # convert from 0-index to 1-index
        while i > 0:
            res += self.bit[i]
            i -= i & -i    
        return res
    
    def lowerLeft(self, w):
        '''
        O(logN)
        A0 ~ Aiの和がw以上となる最小のindex(値)を返す。
        Ai ≧ 0であること。
        '''
        if (w < 0):
            return 0
        total = self.sum(self.N - 1)
        if w > total:
            return -1
        x = 0
        k = 1 << (self.N.bit_length() - 1)
        while k > 0:
            if x + k < self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x
        
    def __str__(self):
        '''
        index0は不使用。
        '''
        return "[" + ", ".join(f'{v}' for v in self.bit) + "]"
    
def main():
    N = int(input())
    E = []
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v, w = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
        E.append((u, v, w))
    bit = BIT(N + 1)
    hl = HLD(N, G)
    hl.build()
    # print(hl.ord)
    # print(hl.heavy_paths)
    for i in range(N - 1):
        u, v, w = E[i]
        u -= 1 
        v -= 1
        if hl.depth_of_node[u] > hl.depth_of_node[v]:
            u, v = v, u
        # print(u, "->", v)
        # print(hl.ord[v], hl.ord[v] + 1, w)
        l, r = hl.subtree_query_range(v)
        bit.add(l, w)
        bit.add(r, -w)
    # print(bit)
    # 0[ord0] --(9)- 3[ord1] -(10)- 4[ord2]
    #   |-(6)- 2[ord3]
    #   |-(3)- 1[ord4]
    # |           6           |           |
    # |     9     |     x     |    -6     |
    # |  0  |  x  |  10 |  x  |  -3 |  x  |
    #    0     1     2     3     4     5    <- ord
    #    [0]   [3]   [4]   [2]   [1] 
    print(bit.sum(hl.ord[0]))
    print(bit.sum(hl.ord[1]))
    print(bit.sum(hl.ord[2]))
    print(bit.sum(hl.ord[3]))
    print(bit.sum(hl.ord[4]))
    print("--")
    print(bit.sum(0))
    print(bit.sum(1))
    print(bit.sum(2))
    print(bit.sum(3))
    print(bit.sum(4))

    # print(bit.sum(hl.ord[0]))
    # print(bit.sum(hl.ord[1]) - bit.sum(hl.ord[0]))
    # print(bit.sum(hl.ord[2]) - bit.sum(hl.ord[0]))
    # print(bit.sum(hl.ord[3]) - bit.sum(hl.ord[0]))
    # print(bit.sum(hl.ord[4]) - bit.sum(hl.ord[3] - 1))

    Q = int(input())
    for _ in range(Q):
        t, a, b = map(int, input().split())
        if t == 1:
            E[a - 1]
        else:
            print(hl.path_query_range(a - 1, b - 1))
            for f, t in hl.path_query_range(a - 1, b - 1):
                p = hl.ord[hl.lca(hl.ord_to_node[f], hl.ord_to_node[t - 1])]
                print(p)
                print(f, t, "#")
                print(bit.sum(t - 1) ,bit.sum(p - 1))
            print("=")

    

    

if __name__ == '__main__':
    main()
