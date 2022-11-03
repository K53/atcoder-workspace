# ------------------------------------------------------------------------------
#     Lazy Binary Index Tree (遅延BIT / フェネック木)
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
# |                       10                      | 
# |           0           |           x           | 
# |     0     |     x     |     0     |     x     | 
# |  0  |  x  |  0  |  x  |  0  |  x  |  10 |  x  |  
# 
# 
# |                       0                       | 
# |           2           |           x           | 
# |     2     |     x     |     0     |     x     | 
# |  0  |  x  |  0  |  x  |  0  |  x  |  -2 |  x  |  
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



class LazyBIT:
    def __init__(self, N):
        self.N = N
        self.bit = [[0] * (self.N + 1) for _ in range(self.N + 1)] # 1-indexedのため
        
    def addSub(self, b, pos, val):
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[b][i] += val
            i += i & -i

    def add(self, l, r, val):
        self.addSub(0, l, -val * (l - 1))
        self.addSub(0, r, val * (r - 1))
        self.addSub(1, l, val)
        self.addSub(1, r, -val)

    def sumSub(self, b, pos):
        res = 0
        i = pos + 1 # convert from 0-index to 1-index
        while i > 0:
            res += self.bit[b][i]
            i -= i & -i    
        return res

    def sum(self, pos):
        print(self.sumSub(0, pos), self.sumSub(1, pos), pos)
        return self.sumSub(0, pos) + self.sumSub(1, pos) * pos

bit = LazyBIT(8)
bit.add(1, 6, 2)
print(bit.bit[0])
print(bit.bit[1])
# bit.add(2, 4, 10)
# print(bit.bit[0])
# print(bit.bit[1])
print(bit.sum(0))
print(bit.sum(1))
print(bit.sum(2))
print(bit.sum(3))
print(bit.sum(4))
print(bit.sum(5))
print(bit.sum(6))
print(bit.sum(7))



# struct BIT {
#     # int n;             // 要素数
#     # vector<T> bit[2];  // データの格納先
#     # BIT(int n_) { init(n_); }
#     # void init(int n_) {
#     #     n = n_ + 1;
#     #     for (int p = 0; p < 2; p++) bit[p].assign(n, 0);
#     # }
#     void add_sub(int p, int i, T x) {
#         for (int idx = i; idx < n; idx += (idx & -idx)) {
#             bit[p][idx] += x;
#         }
#     }
#     void add(int l, int r, T x) {  // [l,r) に加算
#         add_sub(0, l, -x * (l - 1));
#         add_sub(0, r, x * (r - 1));
#         add_sub(1, l, x);
#         add_sub(1, r, -x);
#     }
#     T sum_sub(int p, int i) {
#         T s(0);
#         for (int idx = i; idx > 0; idx -= (idx & -idx)) {
#             s += bit[p][idx];
#         }
#         return s;
#     }
#     T sum(int i) { return sum_sub(0, i) + sum_sub(1, i) * i; }
# };




# class BIT:
#     def __init__(self, N):
#         self.N = N
#         self.bit = [0] * (self.N + 1) # 1-indexedのため
        
#     def add(self, pos, val):
#         '''Add
#             O(logN)
#             posは0-index。内部で1-indexedに変換される。
#             A[pos] += val 
#         '''
#         i = pos + 1 # convert from 0-index to 1-index
#         while i <= self.N:
#             self.bit[i] += val
#             i += i & -i

#     def deleteNonNegative(self, pos, val) -> int:
#         '''Add
#             O(logN)
#             posは0-index。内部で1-indexedに変換される。
#             A[pos] += val 
#         '''
#         actualSubstractVal = min(val, self.sum(pos) - self.sum(pos - 1)) # pos - 1は負になってもself.sum()は大丈夫
#         i = pos + 1 # convert from 0-index to 1-index
#         while i <= self.N:
#             self.bit[i] -= actualSubstractVal
#             i += i & -i
#         return actualSubstractVal

#     def sum(self, pos):
#         ''' Sum
#             O(logN)
#             posは0-index。内部で1-indexedに変換される。
#             Return Sum(A[0], ... , A[pos])
#             posに負の値を指定されるとSum()すなわち0を返すのでマイナスの特段の考慮不要。
#         '''
#         res = 0
#         i = pos + 1 # convert from 0-index to 1-index
#         while i > 0:
#             res += self.bit[i]
#             i -= i & -i    
#         return res
    
#     def lowerLeft(self, w):
#         '''
#         O(logN)
#         A0 ~ Aiの和がw以上となる最小のindex(値)を返す。
#         Ai ≧ 0であること。
#         '''
#         if (w < 0):
#             return 0
#         total = self.sum(self.N - 1)
#         if w > total:
#             return -1
#         x = 0
#         k = 1 << (self.N.bit_length() - 1)
#         while k > 0:
#             if x + k < self.N and self.bit[x + k] < w:
#                 w -= self.bit[x + k]
#                 x += k
#             k //= 2
#         return x
        
#     def __str__(self):
#         '''
#         index0は不使用なので表示しない。
#         '''
#         return "[" + ", ".join(f'{v}' for v in self.bit[1:]) + "]"
