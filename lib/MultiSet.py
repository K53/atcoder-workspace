# ------------------------------------------------------------------------------
#     MultiSet (BIT)
# ------------------------------------------------------------------------------
# 解説
# MultiSet -> HeapDictでは最小値しか取得できなかった。
#             任意の位置の要素を二分探索して取得すること。
#             ※ 制限付き : あらかじめ入りうる要素をクエリ先読みなどでリストにして初期化時に渡す必要あり。
#
# MultiSet [0, 1, 1, 2, 4]
#  - arr [0, 1, 2, 4] # 種類を管理
#  - bit BIT()以下
# |           4           |     |
# |     3     |     x     |     |
# |  1  |  x  |  1  |  x  |  1  |
#    0     1     2     3     4
# 
# - BITのデータの持ち方は以下、累積和を保持 (index = 値 とする。)
# |                      [8]                      | 
# |          [4]          |           x           | 
# |    [2]    |     x     |    [6]    |     x     | 
# | [1] |  x  | [3] |  x  | [5] |  x  | [7] |  x  | # [n]はBIT内部でのindex(1-indexedなので)　気にしなくていい
#    0     1     2     3     4     5     6     7    # index = 値
# 
# Order
#   - insert() : 要素の挿入
#       - O(log(n))
#   - delete() : 要素の削除 <- point!
#       - O(log(n))
#   - getKth() : 小さい方からK番目の要素取得。存在しない場合は-INFが返る。  <- point!
#       - O(log(n))
#   - getKthFromLargest() : 大きい方からK番目の要素取得。存在しない場合は-INFが返る。  <- point!
#       - O(log(n))
#   - countLessThanOrEqualTo() : val以下(≦ val)の要素数を返す。
#       - O(log(n))
#   - countUnder() : val未満(< val)の要素数を返す。
#       - O(log(n))
#   - upperBound(val, k) : valより大きい値において、小さい方からk番目(0-indexed)の値を取得。存在しない場合は-INFが返る。
#       - O(log(n))
#   - lowerBound(val, k) : val以上の値において、小さい方からk番目(0-indexed)の値を取得。存在しない場合は-INFが返る。
#       - O(log(n))
#
# リンク
# - 実装: https://juppy.hatenablog.com/entry/2020/09/03/%E9%A0%86%E5%BA%8F%E4%BB%98%E3%81%8D%E9%9B%86%E5%90%88%E3%82%82%E3%81%A9%E3%81%8D_Python_1
# 
# verify
# - https://atcoder.jp/contests/abc241/tasks/abc241_d
# - https://atcoder.jp/contests/abc253/tasks/abc253_c
# - https://atcoder.jp/contests/abc217/tasks/abc217_d
# ------------------------------------------------------------------------------

from BIT import BIT
import bisect

INF = 10 ** 9

class MultiSet:
    def __init__(self, allVals: "list[int]"):
        print("allValsは重複禁止!!!!入りうる要素を全部入れておく。")
        self.arr = sorted(allVals)
        self.bit = BIT(len(allVals))
        self.ammounts = 0
        
    def insert(self, val: int, count: int = 1):
        idx = bisect.bisect_left(self.arr, val)
        self.bit.add(idx, count)
        self.ammounts += count
    
    def delete(self, val: int, count : int = 1):
        k = bisect.bisect_left(self.arr, val)
        self.bit.add(k, -count)
        self.ammounts -= count
    
    def deleteIgnoreOverSubstract(self, val: int, count : int = 1):
        '''
        MultiSetで保持している個数以上の削除を求められたら無視する。
        '''
        k = bisect.bisect_left(self.arr, val)
        actualSubstractVal = self.bit.deleteNonNegative(k, count)
        self.ammounts -= actualSubstractVal
    
    def getKth(self, k: int) -> int:
        '''getKth
        k : 0-indexed
        小さい方からK番目の値を取得。
        '''
        return self.arr[self.bit.lowerLeft(k + 1)] if 0 <= k < self.ammounts else -INF

    def getKthFromLargest(self, k: int) -> int:
        '''getKth
        k : 0-indexed
        大きい方からK番目の値を取得。
        '''
        return self.arr[self.bit.lowerLeft(self.ammounts - k)] if 0 <= k < self.ammounts else -INF
        
    def countLessThanOrEqualTo(self, val: int) -> int:
        '''
        val以下(≦ val)の要素数を返す。
        '''
        return 0 if val < self.arr[0] else self.bit.sum(bisect.bisect_left(self.arr, val))
    
    def countUnder(self, val: int) -> int:
        '''
        val未満(< val)の要素数を返す。
        '''
        return 0 if val < self.arr[0] else self.bit.sum(bisect.bisect_left(self.arr, val) - 1) # sum()は負なら0が返るのでvalがarrの最下端の数字でもOK

    def upperBound(self, val: int, k: int) -> int:
        '''upperBound
        | - - - -|-|< - - ->|
                 l u
        valより大きい値において、小さい方からk番目の値を取得
        k: 0-indexed
        (存在しないindexでは-INFが返る。)
        '''
        return self.getKth(self.countLessThanOrEqualTo(val) + k)

    def lowerBound(self, val: int, k: int) -> int:
        '''upperBound
        | - - - -|<-| - - ->|
                 l  u
        val以上の値において、小さい方からk番目の値を取得
        k: 0-indexed
        (存在しないindexでは-INFが返る。)
        '''
        return self.getKth(self.countUnder(val) + k)

    def __str__(self):
        res = []
        for i in range(len(self.arr)):
            count = self.bit.sum(i) - (self.bit.sum(i - 1) if i - 1 >= 0 else 0)
            for _ in range(count):
                res.append(i)
        return "[" + ", ".join(f'{self.arr[v]}' for v in res) + "]"

# usage
print("-- MultiSet -------------------------------")
l = [0, 1, 2, 3, 4]
tree = MultiSet(l)
tree.insert(2)
print(tree.bit) # [0, 0, 1, 1, 0]
# |           1           |     |
# |     0     |     x     |     |
# |  0  |  x  |  1  |  x  |  0  |
#    0     1     2     3     4

tree.insert(0, 2)
print(tree.bit) # [2, 2, 1, 3, 0]
# |           3           |     |
# |     2     |     x     |     |
# |  2  |  x  |  1  |  x  |  0  |
#    0     1     2     3     4

tree.delete(0, 1)
print(tree.bit) # [1, 1, 1, 2, 0]
# |           2           |     |
# |     1     |     x     |     |
# |  1  |  x  |  1  |  x  |  0  |
#    0     1     2     3     4

tree.insert(3)
# tree.delete(3, 100) # [1, 1, 1, -97, 0] # 意図しない結果になる。
tree.deleteIgnoreOverSubstract(3, 100) # [1, 1, 1, 2, 0] # 保持している数以上は引き算しない。
print(tree.bit) # [1, 1, 1, 2, 0]

tree.insert(4)
tree.insert(1, 2)
print(tree.bit) # [1, 3, 1, 4, 1]
# |           4           |     |
# |     3     |     x     |     |
# |  1  |  x  |  1  |  x  |  1  |
#    0     1     2     3     4

print(tree) # [0, 1, 1, 2, 4] : OrderBITに含まれる要素一覧を展開したもの。

for val in range(5):
    print(val, "個目までの累積和は", tree.bit.sum(val))
    print(val, "以下は", tree.countLessThanOrEqualTo(val), "個")
    print(val, "未満は", tree.countUnder(val), "個")

print("---")
for val in range(5):
    print(tree.upperBound(val, 0)) # valより大きい数値で小さい方から0番目
    print(tree.upperBound(val, 1)) # valより大きい数値で小さい方から1番目
    print(tree.upperBound(val, 2)) # valより大きい数値で小さい方から2番目
    print(tree.upperBound(val, 3)) # valより大きい数値で小さい方から3番目
    print("---")
print("======")
for val in range(5):
    print(tree.lowerBound(val, 0)) # val以上の数値で小さい方から0番目
    print(tree.lowerBound(val, 1)) # val以上の数値で小さい方から1番目
    print(tree.lowerBound(val, 2)) # val以上の数値で小さい方から2番目
    print(tree.lowerBound(val, 3)) # val以上の数値で小さい方から3番目
    print("---")

#  https://atcoder.jp/contests/abc241/tasks/abc241_d のようにval以下で大きい方からx番目を求めたいなら含める要素をマイナスにすることでOK