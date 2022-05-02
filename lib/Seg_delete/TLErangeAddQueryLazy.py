# ------------------------------------------------------------------------------
#     セグメント木 (1-indexed) Range Add Query (RAQ)
# ------------------------------------------------------------------------------
# 解説
# index 0は使用しない。ノードNの子はノード2Nとノード2N+1
#
# リンク
# 
# 計算量
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E&lang=ja # Range Add Query (RAQ)
# ------------------------------------------------------------------------------

INF = 2 ** 31 - 1
class SegmentTree:
    def __init__(self, monoid: int, bottomLen: int):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen
        self.lazy = [INF] * self.segLen
    
    """遅延評価"""
    def eval(self, k: int):
        # 更新するものがない。
        if self.lazy[k] == INF:
            return
        # 最下層でないなら伝播
        if k < self.offset:
            self.lazy[k * 2] = self.lazy[k]
            self.lazy[k * 2 + 1] = self.lazy[k]
        # 自身を更新
        self.tree[k] = self.lazy[k]
        self.lazy[k] = INF

    """区間最小値取得"""
    def querySub(self, a: int, b: int, k: int, l: int, r: int):
        self.eval(k)
        # 完全に外側
        if r <= a or b <= l:
            return INF
        # 完全に内側
        elif a <= l and r <= b:
            return self.tree[k]
        else:
            vl = self.querySub(a, b, k * 2, l, (l + r) // 2)
            vr = self.querySub(a, b, k * 2 + 1, (l + r) // 2, r)
            return min(vl, vr)

    def query(self, a: int, b: int):
        a += self.offset
        b += self.offset
        return self.querySub(a, b, 1, self.offset, self.segLen)
    
    """区間最小値更新"""
    def updateSub(self, a: int, b: int, x: int, k: int, l: int, r: int):
        self.eval(k)
        # 完全に内側
        if a <= l and r <= b:
            self.lazy[k] = x #
            self.eval(k)
        # 一部が被る
        elif a < r and l < b:
            self.updateSub(a, b, x, k * 2, l, (l + r) // 2)
            self.updateSub(a, b, x, k * 2 + 1, (l + r) // 2, r)
            self.tree[k] = min(self.tree[k * 2], self.tree[k * 2 + 1])
    
    def update(self, a: int, b: int, x: int):
        a += self.offset
        b += self.offset
        self.updateSub(a, b, x, 1, self.offset, self.segLen)

# # Range Add Query
# n = 4
# tr = SegmentTree(initVal=0, bottomLen=2**18)
# tr.rangeAdd(1, 2 + 1, 1)  # セグ木は右側は開区間として計算しているので+1必要。
# tr.rangeAdd(2, 3 + 1, 2)  # セグ木は右側は開区間として計算しているので+1必要。
# tr.rangeAdd(3, 3 + 1, 3)  # セグ木は右側は開区間として計算しているので+1必要。
# print(tr.getPoint(2))
# print(tr.getPoint(3))

n, q = map(int, input().split())
tr = SegmentTree(monoid=INF, bottomLen=2**18)
for _ in range(q):
    c = list(map(int, input().split()))
    if c[0] == 0:
        s, t, x = c[1], c[2], c[3]
        tr.update(s, t + 1, x)
        # print("--")
        # print(tr.tree)
        # print(tr.lazy)
    else:
        s, t = c[1], c[2]
        print(tr.query(s, t + 1))
        # print("--")
        # print(tr.tree)
        # print(tr.lazy)
