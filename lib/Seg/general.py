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
    def __init__(self, monoid: int, bottomLen: int, operation: "function"):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen
        self.operation = operation
        return
    
    """ 1点更新
    O(1)
    """
    def pointUpdateWithoutRebuild(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val          # 各マスの更新方法
        return
    
    """ 全区間更新
    O(bottomLen) # =セグ木の配列長
    """
    def allBuild(self):
        for segIndex in reversed(range(self.offset)):
            if segIndex == 0:
                return
            self.tree[segIndex] = self.operation(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
        return

    """ 1点更新 + リビルド
    O(log(bottomLen))
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val          # 各マスの更新方法
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.operation(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
        return

    def rangeQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = self.monoid                   # クエリの初期値
        while l < r:
            if l % 2 == 1:
                res = self.operation(res, self.tree[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                res = self.operation(res, self.tree[r - 1])
                r -= 1
            r //= 2
        return res

    """ 二分探索
    O(log(bottomLen))
    """
    def queryKthItem(self, K: int):
        index = 1   # セグ木の頂点が開始
        restK = K
        while index < self.offset:  # 最下層に到達するまで回す
            if restK <= self.tree[2 * index]:   # 右に行く条件
                index = 2 * index
            else:                               # 左に行く条件
                restK -= self.tree[2 * index]   # 左に進む場合は右側の分を差し引く。
                index = 2 * index + 1
        return index - self.offset

def add(a: int, b: int):
    return a + b

Q = 5
queries = [(0, 1, 1), (0, 2, 2), (0, 3, 3), (1, 1, 2), (1, 2, 2)]
tr = SegmentTree(monoid=0, bottomLen=2**18, operation=add)
for i in range(Q):
    query = queries[i]
    if query[0] == 0:
        tr.pointUpdate(query[1], query[2])
    else:
        ans = tr.rangeQuery(query[1], query[2] + 1)
        print(ans)




# class SegmentTree:
#     def __init__(self, monoid: int, bottomLen: int):
#         self.monoid = monoid
#         self.bottomLen = bottomLen
#         self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
#         self.segLen = self.bottomLen * 2
#         self.tree = [monoid] * self.segLen

#     def pointAdd(self, index: int, val: int):
#         segIndex = index + self.offset
#         self.tree[segIndex] += val    # 任意の変更
#         while True:
#             segIndex //= 2
#             if segIndex == 0:
#                 break
#             self.tree[segIndex] = self.tree[segIndex * 2] + self.tree[segIndex * 2 + 1]    # 任意の演算
#         return

#     """ 区間和 (RSQ)
#     """
#     def rangeSumQuery(self, l: int, r: int):
#         l += self.offset
#         r += self.offset
#         res = 0
#         while l < r:
#             if l % 2 == 1:
#                 res += self.tree[l]    # 任意の演算
#                 l += 1
#             l //= 2
#             if r % 2 == 1:
#                 res += self.tree[r - 1]    # 任意の演算
#                 r -= 1
#             r //= 2
#         return res

# # Range Sum Query
# tr = SegmentTree(monoid=0, bottomLen=2**18) ### !! デバッグ用に小さいレンジにした時は提出前に直すこと
# tr.pointAdd(1, 1)
# tr.pointAdd(2, 2)
# tr.pointAdd(3, 3)
# print(tr.rangeSumQuery(1, 2 + 1)) # セグ木は右側は開区間として計算しているので+1必要。

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja
# n, q = map(int, input().split())
# tr = SegmentTree(initVal=0, bottomLen=2**18)
# for _ in range(q):
#     com, a, b = map(int, input().split())
#     if com == 0:
#         tr.pointAdd(a, b)
#     else:
#         print(tr.rangeSumQuery(a, b + 1))