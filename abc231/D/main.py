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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    d = defaultdict(int)
    uf = UnionFind(N)
    for aa, bb in zip(A, B):
        d[aa - 1] += 1
        d[bb - 1] += 1
        uf.union(aa - 1, bb - 1)
    for g in uf.all_group_members().values():
        c1 = 0
        if len(g) == 1:
            continue
        for i in g:
            if d[i] > 2:
                print(NO)
                return
            if d[i] == 1:
                c1 += 1
        if c1 == 0 or c1 % 2 == 1:
            print(NO)
            return
    print(YES)
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
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
