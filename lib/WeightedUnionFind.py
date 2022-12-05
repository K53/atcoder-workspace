# ------------------------------------------------------------------------------
#     ポテンシャル付き/重み付き Union-Find木
# ------------------------------------------------------------------------------
# 解説
# - 要素数Nのリストを持ち、根の要素の番号を格納する。
# - その要素自体が根の場合はマイナスを付して格納しておく。
# 
# リンク
# - https://qiita.com/drken/items/cce6fc5c579051e64fab (メイン)
# - https://at274.hatenablog.com/entry/2018/02/03/140504 (参考)
# 
# 計算量
# - α(N) ・・・ Ackermann 関数の逆関数であり、ほぼ定数。
# 
# verify
# - https://yukicoder.me/problems/no/1390
# - https://atcoder.jp/contests/abl/tasks/abl_c
# - https://atcoder.jp/contests/abc229/tasks/abc229_e
# ------------------------------------------------------------------------------
from collections import defaultdict
INF = 10 ** 16

class WeightedUnionFind():
    def __init__(self, n):
        self.n = n
        self.group_num = n
        self.parents = [-1] * n # 負で表現したサイズ
        self.diff_weight = [0] * n # 属する集合の親からの距離

    """ 要素xの親を取得。"""
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            r = self.find(self.parents[x]) # 経路圧縮
            self.diff_weight[x] += self.diff_weight[self.parents[x]]; # 累積和をとる
            self.parents[x] = r
            return self.parents[x]

    """ 2つの要素の併合。
    すでに同じ集合に属する場合はFalseを返す。
    """
    def union(self, x, y, w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False

        # xの方がサイズが大きい状態にする。parentsは中身負なので注意
        if self.parents[x] > self.parents[y]:
            x, y = y, x
            w = -w

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.group_num -= 1
        self.diff_weight[y] = w; 
        return True
    
    def weight(self, x: int) -> int:
        self.find(x) # 経路圧縮
        return self.diff_weight[x]

    """ 2点x, y間の距離を返す。
    同一の集合に属さない場合は INF を返す。
    """
    def diff(self, x: int, y: int) -> int:
        # 
        if not self.same(x, y):
            return INF
        return self.weight(y) - self.weight(x)

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

    """ 集合の個数を取得。 v2
    計算量 : O(1)
    """
    def group_count_v2(self):
        return self.group_num

    """ 集合の個数を取得。 v1
    計算量 : O(N)
    """
    def group_count_v1(self):
        return len(self.roots())

    """ 全集合の要素一覧を取得。
    計算量 : O(N)
    """
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append((member, self.diff_weight[member]))
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
# Usage
N = 5
wuf = WeightedUnionFind(N)
wuf.union(2, 3, 10)
wuf.union(4, 2, 1)
wuf.union(4, 3, 1000000) # False となり無視される。
print(wuf)
print(wuf.diff_weight)
"""
0: [(0, 0)]
1: [(1, 0)]
2: [(2, 0), (3, 10), (4, -1)]
[0, 0, 0, 10, -1]
"""

# 2 -> 3 の向きに距離10
# 4 -> 2 の向きに距離1
# 初期実行時に親は"2"となるのでdiff_weightには負の値となる
print(wuf.diff(2, 3)) # 10
print(wuf.diff(2, 4)) # -1
print(wuf.diff(4, 2)) # 1
print(wuf.diff(3, 4)) # -11
