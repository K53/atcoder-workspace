#!/usr/bin/env python3
import sys
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    """ 要素xの値を取得。"""
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    """ 2つの要素の併合。"""
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return

    """ 要素xの属する集合の要素数を取得。"""
    def size(self, x):
        return -self.parents[self.find(x)]

    """ 2つの要素が同一の集合に属するか。"""
    def same(self, x, y):
        return self.find(x) == self.find(y)

    """ 要素xと同一の集合の要素を全取得。
    計算量 : O(N)
    """
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    """ 各集合の根を全取得。
    計算量 : O(N)
    """
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    """ 集合の個数を取得。
    計算量 : O(N)
    """
    def group_count(self):
        return len(self.roots())

    """ 全集合の要素一覧を取得。
    計算量 : O(N)
    """
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    

class Kruskal():
    def __init__(self, N: int) -> None:
        # self.minimumG = [[] for _ in range(N)] # 全域最小木自体が欲しい場合にはこれを有効にする。
        self.edges = []
        self.uf =  UnionFind(N)
        self.minimunCost = 0
        return
    
    def addEdge(self, a: int, b: int, cost: int):
        self.edges.append((cost, a, b))
        return
    
    def build(self):
        for cost, a, b in sorted(self.edges):
            if cost > 0 and self.uf.same(a, b):
                continue
            self.minimunCost += cost
            self.uf.union(a, b)
            # --- 全域最小木自体を構築 ---
            # self.minimumG[a].append(b)
            # self.minimumG[b].append(a)
        return self.minimunCost

def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    ks = Kruskal(N)
    for aa, bb, cc in zip(A, B, C):
        ks.addEdge(aa - 1, bb - 1, cc)
    d = ks.build()
    print(sum(C) - d)
    return


# Generated by 2.8.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
