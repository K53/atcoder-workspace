#!/usr/bin/env python3
from typing import List, Tuple, Callable, TypeVar
import sys

input = sys.stdin.readline

def main():
    class BIT:
        def __init__(self, N):
            self.N = N
            self.A = [0] * (N + 1)

        def build(self, A):
            """build BIT with given list"""
            for i, a in enumerate(A):
                self.A[i + 1] = a
            for i in range(1, self.N):
                if i + (i & -i) > self.N:
                    continue
                self.A[i + (i & -i)] += self.A[i]

        def add(self, i, x):
            """add x to i-th element (0-indexed)"""
            # assert 0 <= i < self.N
            i += 1
            while i <= self.N:
                self.A[i] += x
                i += i & -i

        def sum(self, i):
            """return sum(A[:i])"""
            assert 0 <= i <= self.N
            s = 0
            while i > 0:
                s += self.A[i]
                i -= i & -i
            return s

        def range_sum(self, l, r):
            """return sum(A[l:r])"""
            return self.sum(r) - self.sum(l)

    class HLD:
        # reference: https://codeforces.com/blog/entry/53170
        def __init__(self, N, G, root: int = 0):
            self.N = N
            self.G = G
            self.root = root

            # self.D = [0] * self.N
            # self.parent_nodes = [-1] * self.N
            # self.partial_tree_size = [0] * self.N
            self.next_heavy_nodes = [-1] * self.N        # next_heavy_nodes[i] := heavy-pathにおいてノードiの次ノード番号 (0-indexed)
            self.parent_nodes = [None] * self.N               # parent_nodes[i] := ノードiの親ノード番号 (0-indexed)
            self.partial_tree_size = [None] * self.N          # partial_tree_size[i] := ノードi以下の部分木のサイズ
            
            self.top = [0] * self.N

            self.ord = [None] * self.N

            # self._dfs_sz()
            self._dfs()
            self._dfs_hld()

        def path_query_range(self, u: int, v: int, is_edge_query: bool = False) -> List[Tuple[int, int]]:
            """return list of [l, r) ranges that cover u-v path"""
            ret = []
            while True:
                if self.ord[u] > self.ord[v]:
                    u, v = v, u
                if self.top[u] == self.top[v]:
                    ret.append((self.ord[u] + is_edge_query, self.ord[v] + 1))
                    return ret
                ret.append((self.ord[self.top[v]], self.ord[v] + 1))
                v = self.parent_nodes[self.top[v]]

        def subtree_query_range(self, v: int) -> Tuple[int, int]:
            """return [l, r) range that cover vertices of subtree v"""
            return (self.ord[v], self.ord[v] + self.partial_tree_size[v])

        def lca(self, u, v):
            while True:
                if self.ord[u] > self.ord[v]:
                    u, v = v, u
                if self.top[u] == self.top[v]:
                    return u
                v = self.parent_nodes[self.top[v]]

        def _dfs(self, cur):
            sub_node_count = 1              # そのノード(を含む)配下の子ノード数
            heavy_path = None               # そのノードからのheavy-path
            max_heavy_path_length = 0       # 最大のheavy-path長
            for next in G[cur]:
                if self.parent_nodes[cur] == next:
                    continue
                self.parent_nodes[next] = cur
                sub_node_total_count = self._dfs(next)
                # より長いパスが見つかったなら
                # heavy-pathとしてその子ノードの番号を仮置きする。
                if max_heavy_path_length < sub_node_total_count:
                    heavy_path = next
                    max_heavy_path_length = sub_node_total_count
                sub_node_count += sub_node_total_count
            self.partial_tree_size[cur] = sub_node_count
            self.next_heavy_nodes[cur] = heavy_path
            return sub_node_count

        # def _dfs_sz(self):
        #     stack = [(self.root, -1)]
        #     while stack:
        #         v, p = stack.pop()
        #         if v < 0:
        #             v = ~v
        #             self.partial_tree_size[v] = 1
        #             for i, dst in enumerate(self.G[v]):
        #                 if dst == p:
        #                     continue
        #                 self.partial_tree_size[v] += self.partial_tree_size[dst]
        #                 # v -> G[v][0] will be heavy path
        #                 if self.partial_tree_size[self.G[v][0]] < self.partial_tree_size[dst]:
        #                     self.G[v][0], self.G[v][i] = self.G[v][i], self.G[v][0]
        #         else:
        #             if ~p:
        #                 # self.D[v] = self.D[p] + 1
        #                 self.parent_nodes[v] = p
        #             # avoid first element of E[v] is parent of vertex v if v has some children
        #             if len(self.G[v]) >= 2 and self.G[v][0] == p:
        #                 self.G[v][0], self.G[v][1] = self.G[v][1], self.G[v][0]
        #             stack.append((~v, p))
        #             for dst in self.G[v]:
        #                 if dst == p:
        #                     continue
        #                 stack.append((dst, v))

        def _dfs_hld(self):
            stack = [(self.root, -1)]
            cnt = 0
            while stack:
                v, p = stack.pop()
                self.ord[v] = cnt
                cnt += 1
                heavy_path_idx = len(self.G[v]) - 1
                for i, dst in enumerate(self.G[v][::-1]):
                    if dst == p:
                        continue
                    # top[dst] is top[v] if v -> dst is heavy path otherwise dst itself
                    self.top[dst] = self.top[v] if i == heavy_path_idx else dst
                    stack.append((dst, v))

    N = 8
    M = 7
    A = [0, 0, 0, 1, 1, 5, 5]
    B = [1, 2, 3, 4, 5, 6, 7]
    G = [[] for _ in range(N)]
    for i in range(M):
        G[A[i]].append(B[i])
        G[B[i]].append(A[i])

    # N = int(input())
    # E = [[] for _ in range(N)]
    # for _ in range(N - 1):
    #     u, v = map(int, input().split())
    #     u -= 1
    #     v -= 1
    #     E[u].append(v)
    #     E[v].append(u)

    # solver = HLD(N, E)
    solver = HLD(N, G)

    # print(solver.D)
    print(solver.parent_nodes)
    print(solver.partial_tree_size)
    print(solver.top)
    return
    bit = BIT(N)
    Q = int(input())
    for _ in range(Q):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        for l, r in solver.path_query_range(a, b):
            bit.add(l, 1)
            bit.add(r, -1)
    ans = 0
    for i in range(N):
        cnt = bit.sum(i + 1)
        ans += (1 + cnt) * cnt // 2
    print(ans)

if __name__ == '__main__':
    main()