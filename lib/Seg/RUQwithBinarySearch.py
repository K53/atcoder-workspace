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
# - https://atcoder.jp/contests/arc033/tasks/arc033_3
# ------------------------------------------------------------------------------

class SegmentTree:
    def __init__(self, monoid: int, bottomLen: int):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen

    """ 一点更新 区間和 (RSQ)
    tree[index] += val
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = val # 一点更新
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.tree[segIndex * 2] + self.tree[segIndex * 2 + 1] # 区間和の算出
        return

    """ 区間和 (RSQ)
    """
    def queryKthItem(self, K: int):
        index = 1
        restK = K
        while index < self.offset:
            if restK <= self.tree[2 * index]:
                index = 2 * index
            else:
                restK -= self.tree[2 * index] # 左に進む場合は右側の分を差し引く。
                index = 2 * index + 1
        return index - self.offset

# https://atcoder.jp/contests/arc033/tasks/arc033_3
query = [
    (1, 11),
    (1, 29),
    (1, 89),
    (2, 2),
    (2, 2)
]
tr = SegmentTree(monoid=0, bottomLen=2**18)
for q in query:
    if q[0] == 1:
        num = q[1] - 1
        tr.pointUpdate(num, 1)
    else:
        k = q[1]
        num = tr.queryKthItem(k)
        print(num + 1)
        tr.pointUpdate(num, 0)