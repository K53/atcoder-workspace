# ------------------------------------------------------------------------------
#     セグメント木 (1-indexed) Range Update Query (RUQ)
# ------------------------------------------------------------------------------
# 解説
# index 0は使用しない。ノードNの子はノード2Nとノード2N+1
#
# リンク
# 
# 計算量
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D&lang=ja # Range Update Query (RUQ)
# - https://atcoder.jp/contests/past202109-open/tasks/past202109_j
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
    def rangeUpdate(self, l: int, r: int, val: int):
        # 最下層のオフセットに変換
        l += self.offset
        r += self.offset
        
        # 最も長い区間を選択して値を反映していく。
        while l < r:
            if l % 2 == 1:
                self.tree[l] += val # 任意の演算方法に変換する (今回は加算)
                l += 1
            l //= 2
            if r % 2 == 1:
                self.tree[r - 1] += val # 任意の演算方法に変換する (今回は加算)
                r -= 1
            r //= 2
        return
    
    """ 一点取得
    """
    def getPoint(self, index: int):
        # 最下層のオフセットに変換
        segIndex = index + self.offset
        res = self.tree[segIndex]
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            res += self.tree[segIndex]  # 全ての区間の情報を集計 任意の演算方法に変換する (今回は加算)
        return res

# # Range Update Query
# n = 4
# tr = SegmentTree(initVal=0, bottomLen=2**18)
# tr.rangeUpdate(1, 2 + 1, 1)  # セグ木は右側は開区間として計算しているので+1必要。
# tr.rangeUpdate(2, 3 + 1, 2)  # セグ木は右側は開区間として計算しているので+1必要。
# tr.rangeUpdate(3, 3 + 1, 3)  # セグ木は右側は開区間として計算しているので+1必要。
# print(tr.getPoint(2))
# print(tr.getPoint(3))


n, q = map(int, input().split())
INF = 2 ** 31 - 1
tr = SegmentTree(initVal=INF, bottomLen=2**18)
for _ in range(q):
    a = list(map(int, input().split()))
    if a[0] == 0:
        tr.rangeUpdate(a[1], a[2] + 1, a[3])
    else:
        print(tr.getPoint(a[1]))