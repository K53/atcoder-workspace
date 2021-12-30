# ------------------------------------------------------------------------------
#     セグメント木 (1-indexed) Range Sum Query (RSQ)
# ------------------------------------------------------------------------------
# 解説
# index 0は使用しない。ノードNの子はノード2Nとノード2N+1
#
# リンク
# 
# 計算量
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja # Range Sum Query (RSQ)
# ------------------------------------------------------------------------------

class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int):
        self.initVal = initVal
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    """ 一点加算 区間和 (RSQ)
    tree[index] += val
    """
    def pointAdd(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.tree[segIndex * 2] + self.tree[segIndex * 2 + 1]
        return

    """ 区間和 (RSQ)
    """
    def rangeSumQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = 0
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            l //= 2
            if r % 2 == 1:
                res += self.tree[r - 1]
                r -= 1
            r //= 2
        return res

# Range Sum Query
tr = SegmentTree(initVal=0, bottomLen=2**18)
tr.pointAdd(1, 1)
tr.pointAdd(2, 2)
tr.pointAdd(3, 3)
print(tr.rangeSumQuery(1, 2 + 1)) # セグ木は右側は開区間として計算しているので+1必要。

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja
# n, q = map(int, input().split())
# tr = SegmentTree(initVal=0, bottomLen=2**18)
# for _ in range(q):
#     com, a, b = map(int, input().split())
#     if com == 0:
#         tr.pointAdd(a, b)
#     else:
#         print(tr.rangeSumQuery(a, b + 1))