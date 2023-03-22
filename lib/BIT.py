# ------------------------------------------------------------------------------
#     Binary Index Tree (BIT / フェネック木)
# ------------------------------------------------------------------------------
# 解説
# BITの index = 値 とする。
#
# - (i & -i) → 最下位ビットを取得できる。
#   - 00101110 01011000 (=  i)
#   - 11010001 10101000 (= -i)
#   - 00000000 00001000 (= i & -i)
# - データの持ち方は以下
# |                      [8]                      | 
# |          [4]          |           x           | 
# |    [2]    |     x     |    [6]    |     x     | 
# | [1] |  x  | [3] |  x  | [5] |  x  | [7] |  x  |  
# 
# iに最下位ビットを加算すると遡上し、減算すると降下する。
# 
# Order
#   - add() : 要素の追加
#       - O(log(n))
#   - sum() : 累積和の算出
#       - O(log(n))
#   - lowerLeft() : 累積和上の二分探索
#       - O(log(n))
#
# リンク
# - https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree (イメージ)
# - 実装: https://juppy.hatenablog.com/entry/2020/09/03/%E9%A0%86%E5%BA%8F%E4%BB%98%E3%81%8D%E9%9B%86%E5%90%88%E3%82%82%E3%81%A9%E3%81%8D_Python_1
# - https://scrapbox.io/pocala-kyopro/%E8%BB%A2%E5%80%92%E6%95%B0 (転倒数)
# - http://hos.ac/slides/20140319_bit.pdf
# - https://algo-logic.info/binary-indexed-tree/ (old実装)
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=jp
# ------------------------------------------------------------------------------
class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (self.N + 1) # 1-indexedのため
        
    def add(self, pos, val):
        '''Add
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            A[pos] += val 
        '''
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] += val
            i += i & -i

    def deleteNonNegative(self, pos, val) -> int:
        '''Add
            O(logN)
            ※ multisetで使用される関数
            posは0-index。内部で1-indexedに変換される。
            すでにMultiSetに含まれている個数以上は削除されない。
            A[pos] -= val 
        '''
        actualSubstractVal = min(val, self.sum(pos) - self.sum(pos - 1)) # pos - 1は負になってもself.sum()は大丈夫
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] -= actualSubstractVal
            i += i & -i
        return actualSubstractVal

    def sum(self, pos):
        ''' Sum
            0からposまでの和を返す(posを含む)
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            Return Sum(A[0], ... , A[pos])
            posに負の値を指定されるとSum()すなわち0を返すのでマイナスの特段の考慮不要。
        '''
        res = 0
        i = pos + 1 # convert from 0-index to 1-index
        while i > 0:
            res += self.bit[i]
            i -= i & -i    
        return res
    
    def lowerLeft(self, w):
        '''
        O(logN)
        A0 ~ Aiの和がw以上となる最小のindex(値)を返す。
        Ai ≧ 0であること。
        '''
        if (w < 0):
            return 0
        total = self.sum(self.N - 1)
        if w > total:
            return -1
        x = 0
        k = 1 << (self.N.bit_length() - 1)
        while k > 0:
            if x + k < self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x
        
    def __str__(self):
        '''
        index0は不使用なので表示しない。
        '''
        return "[" + ", ".join(f'{v}' for v in self.bit[1:]) + "]"
    
# usage
bit = BIT(4)
bit.add(2, 1)
# |           1            |
# |     0     |     x      |
# |  0  |  x  |  1  |  x   |
#    0     1     2     3

bit.add(1, 1)
# |           2            |
# |     1     |     x      |
# |  0  |  x  |  1  |  x   |
#    0     1     2     3

bit.add(3, 1)
# |           3            |
# |     1     |     x      |
# |  0  |  x  |  1  |  x   |
#    0     1     2     3

bit.add(2, 1)
# |           4            |
# |     1     |     x      |
# |  0  |  x  |  2  |  x   |
#    0     1     2     3

print(bit) # [0, 1, 2, 4]

# 0からの累積和算出
print(">", bit.sum(0)) # 0
print(">", bit.sum(1)) # 1
print(">", bit.sum(2)) # 3
print(">", bit.sum(3)) # 4

# 和が val 以上になるindex
print(bit.lowerLeft(-100)) # 0 和-100以上になるindex(値)
print(bit.lowerLeft(1)) # 1 和1以上になるindex(値)
print(bit.lowerLeft(2)) # 2 和2以上になるindex(値)
print(bit.lowerLeft(100)) # -1 和2以上になるindex(値)

# # 転倒数(要素重複対応)
# l = [3, 0, 5, 4, 2]
# bit = BIT(max(l) + 1)
# ans = 0

# # 既出のもの(=自分より左側のもの)からBITに記入されることを利用している。
# # 大小比較のIFとかがないのもその理由。
# for i in range(len(l)):
#     val = l[i]
#     print(bit.bit[1:])
#     print(val, ":",  bit.sum(val)) # 今の位置iよりも左側に、今の位置の数valよりも大きい数は何個あるか。
#     ans += i - bit.sum(val) 
#     bit.add(val, 1)

# print(bit.bit[1:])
# print(ans)


