# ------------------------------------------------------------------------------
#     遅延セグメント木 (1-indexed)
# ------------------------------------------------------------------------------
# 解説
# 
#
# リンク
# - https://tsutaj.hatenablog.com/entry/2017/03/30/224339
# 
# 計算量
# 
# verify
# - 
# ------------------------------------------------------------------------------
class LazySegmentTree:
    def __init__(self, monoid: int, bottomLen: int, func: "function(int, int)"):
        self.monoid = monoid
        self.func = func
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen
        self.lazy = [0] * self.segLen

