# ------------------------------------------------------------------------------
#     Union-Find木
# ------------------------------------------------------------------------------
# 解説
# - 要素数Nのリストを持ち、根の要素の番号を格納する。
# - その要素自体が根の場合はマイナスを付して格納しておく。
# 
# リンク
# - https://note.nkmk.me/python-union-find/
# 
# 計算量
# - α(N) ・・・　Ackermann 関数の逆関数であり、ほぼ定数。
# 
# verify
# - https://yukicoder.me/problems/no/1390
# ------------------------------------------------------------------------------
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
    
# Usage
N = 5
uf = UnionFind(N)
uf.union(2, 3)
print(uf)
"""
0: [0]
1: [1]
2: [2, 3]
4: [4]
"""
