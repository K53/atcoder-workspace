# ------------------------------------------------------------------------------
#     セグメント木 (1-indexed) Range Minimum Query (RMQ)
# ------------------------------------------------------------------------------
# 解説
# index 0は使用しない。ノードNの子はノード2Nとノード2N+1
#
# リンク
# 
# 計算量
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A&lang=ja # Range Minimum Query (RMQ)
# ------------------------------------------------------------------------------
class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int):
        self.initVal = initVal
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    """ 一点更新 区間最小値 (RMQ)
    tree[index] = val
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = min(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
        return

    """ 区間最小値 (RMQ)
    """
    def rangeMinQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = self.initVal
        while l < r:
            if l % 2 == 1:
                res = min(res, self.tree[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                res = min(res, self.tree[r - 1])
                r -= 1
            r //= 2
        return res

# Range Minimum Query
INF = 10 ** 9
tr = SegmentTree(initVal=INF, bottomLen=2**18)
tr.pointUpdate(1, 1)
tr.pointUpdate(2, 2)
tr.pointUpdate(3, 3)
print(tr.rangeMinQuery(1, 2 + 1)) # セグ木は右側は開区間として計算しているので+1必要。
