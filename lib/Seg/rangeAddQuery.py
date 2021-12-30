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

class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int):
        self.initVal = initVal
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    """ 区間加算 (RAQ)
    """
    def rangeAdd(self, l: int, r: int, val: int):
        l += self.offset
        r += self.offset
        while l < r:
            if l % 2 == 1:
                self.tree[l] += val
                l += 1
            l //= 2
            if r % 2 == 1:
                self.tree[r - 1] += val
                r -= 1
            r //= 2
        return
    
    """ 一点取得
    """
    def getPoint(self, index: int):
        segIndex = index + self.offset
        res = self.tree[segIndex]
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            res += self.tree[segIndex]
        return res


# # Range Add Query
# n = 4
# tr = SegmentTree(initVal=0, bottomLen=2**18)
# tr.rangeAdd(1, 2 + 1, 1)  # セグ木は右側は開区間として計算しているので+1必要。
# tr.rangeAdd(2, 3 + 1, 2)  # セグ木は右側は開区間として計算しているので+1必要。
# tr.rangeAdd(3, 3 + 1, 3)  # セグ木は右側は開区間として計算しているので+1必要。
# print(tr.getPoint(2))
# print(tr.getPoint(3))

n, q = map(int, input().split())
tr = SegmentTree(initVal=0, bottomLen=2**18)
for _ in range(q):
    com, a, b = map(int, input().split())
    if com == 0:
        tr.rangeAdd(a, b)
