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


N = 12
A = [0, 0, 1, 2, 2, 3, 5, 5, 6, 9, 9]
B = [1, 2, 3, 4, 5, 9, 6, 7, 8, 10, 11]
G = [[] for _ in range(N)]
# 木としての深さ depth_of_node
#               [0]                 --- depth 0
#              /   \
#            [1]   [2]              --- depth 1
#           /     /   \
#         [3]   [4]   [5]           --- depth 2
#        /           /   \
#      [9]         [6]   [7]        --- depth 3
#     /   \       /  
#   [10]  [11]  [8]                 --- depth 4
#
# Heavy-pathとしての深さ depth_of_heavy_path
# Depth 0: [0] -------------------- [2] - [5] - [6] - [8]
#           |                        |     |
# Depth 1: [1] - [3] - [9] - [10]   [4]   [7] 
#                       |
# Depth 2:             [11]
for i in range(N - 1):
    G[A[i]].append(B[i])
    G[B[i]].append(A[i])

hl = HLD(N, G)
hl.build()

print("depth_of_node", hl.depth_of_node)
# [0, 1, 1, 2, 2, 2, 3, 3, 4, 3, 4, 4]
print("next_heavy_nodes", hl.next_heavy_nodes)
# [2, 3, 5, 9, None, 6, 8, None, None, 10, None, None]
print("parent_nodes", hl.parent_nodes)
# [None, 0, 0, 1, 2, 2, 5, 5, 6, 3, 9, 9]
print("partial_tree_size", hl.partial_tree_size)
# [12, 5, 6, 4, 1, 4, 2, 1, 1, 3, 1, 1]
print("heavy_paths", hl.heavy_paths)
# [[0, 2, 5, 6, 8], [7], [4], [1, 3, 9, 10], [11]]
print("depth_of_heavy_path", hl.depth_of_heavy_path)
# [0, 1, 1, 1, 2]
print("to_heavy_path_index", hl.to_heavy_path_index) # ノードiがheavy_pathsのどのHeavy-Pathに属するか
# [0, 3, 0, 3, 2, 0, 0, 1, 0, 3, 3, 4]
print("indices_in_heavy_path", hl.indices_in_heavy_path)  
# [0, 0, 1, 1, 0, 2, 3, 0, 4, 2, 3, 0]
print("heads", hl.heads) # ノードiが属するheavy_paths内の先頭ノード番号
# [0, 1, 0, 1, 4, 0, 0, 7, 0, 1, 1, 11]
print("ord", hl.ord) # 同一のheavy_pathsには連続した番号が振られるよう調整された番号。ノードiはord[i]に対応。
# [0, 7, 1, 8, 6, 2, 3, 5, 4, 9, 10, 11]   -> セグ木などのindexに対応させるために使う。
# Depth 0: [0(ord:0)] ------------------------------------------ [2(ord:1)] - [5(ord:2)] - [6(ord:3)] - [8(ord:4)]
#           |                                                     |            |
# Depth 1: [1(ord:7)] - [3(ord:8)] - [9(ord:9)] - [10(ord:10)]   [4(ord:6)]   [7(ord:5)] 
#                                     |
# Depth 2:                           [11(ord:11)]


l1 = (hl.path_query_range(3, 5)) 
print(l1)
# [(7, 9), (0, 3)]
l2 = (hl.path_query_range(5, 3)) # a/bの順に依存しない
print(l2)
# [(7, 9), (0, 3)]
l3 = (hl.path_query_range(7, 11)) 
print(l3)
# [(11, 12), (7, 10), (5, 6), (0, 3)]

# ノード3を根とする部分木の範囲を取得
b1 = hl.subtree_query_range(3)
print(b1)
# (8, 12)

# 木の特定の区間にだけ加減算する場合。
from BIT import BIT
bit = BIT(N + 1)
# Depth 0: [0(ord:0)] ----------------------------------- [2(ord:1)] - [5(ord:2)] - [x] - [x]
#           |                                              |            |
# Depth 1: [1(ord:7)] - [3(ord:8)] - [9(ord:9)] - [x]     [x]          [7(ord:5)] 
#                                     |
# Depth 2:                           [11(ord:11)]


for l, r in hl.path_query_range(7, 11): # [(11, 12), (7, 10), (5, 6), (0, 3)]
    bit.add(l, 1)
    bit.add(r, -1)

print(bit)
# |                                   0                                   |  x  |
# |                       1                       |           x           |  x  |
# |           0           |           x           |           x           |  x  |
# |     1     |     x     |     1     |     x     |     0     |     x     |  x  |
# |  1  |  x  |  0  |  x  |  0  |  x  |  -1 |  x  |  0  |  x  |  -1 |  x  |  -1 |
#    0     1     2     3     4     5     6     7     8     9     10    11    12

acc = [bit.sum(i) for i in range(N)] # 先頭0からの累積和になる
print(acc)
# [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1]

for l, r in hl.path_query_range(1, 3):  # [(7, 9)]
    bit.add(l, 1)
    bit.add(r, -1)

acc = [bit.sum(i) for i in range(N)] # 先頭0からの累積和になる
print(acc)
# [1, 1, 1, 0, 0, 1, 0, 2, 2, 1, 0, 1]