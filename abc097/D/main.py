#!/usr/bin/env python3
import sys
from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.group_num = n
        self.parents = [-1] * n # サイズ

    def find(self, x):
        """ 要素xの親を取得。"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x]) # 経路圧縮
            return self.parents[x]

    def union(self, x, y):
        """ 2つの要素の併合。"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.group_num -= 1
        return

    def size(self, x):
        """ 要素xの属する集合の要素数を取得。"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """ 2つの要素が同一の集合に属するか。"""
        return self.find(x) == self.find(y)

    def members(self, x):
        """ 要素xと同一の集合の要素を全取得。
        計算量 : O(N)
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """ 各集合の根を全取得。
        計算量 : O(N)
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count_v2(self):
        """ 集合の個数を取得。 v2
        計算量 : O(1)
        """
        return self.group_num

    def group_count_v1(self):
        """ 集合の個数を取得。 v1
        計算量 : O(N)
        """
        return len(self.roots())

    def all_group_members(self):
        """ 全集合の要素一覧を取得。
        計算量 : O(N)
        """
        group_members = defaultdict(set)
        for member in range(self.n):
            group_members[self.find(member)].add(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def solve(N: int, M: int, p: "List[int]", x: "List[int]", y: "List[int]"):
    uf = UnionFind(N)
    ans = 0
    for xx, yy in zip(x, y):
        uf.union(xx - 1, yy - 1)
    for k, v in uf.all_group_members().items():
        for i in v:
            c = p[i] - 1
            if c in v:
                ans += 1
    print(ans)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, p, x, y)

if __name__ == '__main__':
    main()
