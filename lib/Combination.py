# ------------------------------------------------------------------------------
#     組み合わせ(Compination, nCr)
# ------------------------------------------------------------------------------
# 解説
# - 組み合わせの総数を出力。
# 
# リンク
# - 
# 
# 計算量
# - O(log(r))以下程度(概算)
# - https://qiita.com/ageprocpp/items/f6661deaa09dda124132
# 
# verify
# - https://atcoder.jp/contests/abc185/tasks/abc185_c
# - https://atcoder.jp/contests/abc034/tasks/abc034_c
# ------------------------------------------------------------------------------
# 階乗の逆元の前処理をしてMODとる場合は->次のCombunationクラスへ
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r + 1):                    # p番目について、
        pivot = denominator[p - 1]              # pivotで約分を試みる。
        if pivot > 1:                           # ただし、pivotが1、すなわちすでに割り尽くされているならp番目は飛ばす。
            offset = (n - r) % p
            for k in range(p - 1, r, p):            # p番目を約分できるということはp番目からpの倍数番目も約分可能なので実施する。
                numerator[k - offset] //= pivot
                denominator[k] //= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


# Udage
print(cmb(10, 2)) # = 10C2 = 10 * 9 // 2 * 1
"-> 45"

# ------------------------------------------------------------------------------
#     組み合わせ(Compination, nCr)
# ------------------------------------------------------------------------------
# 解説
# - mod下のnCr算出。
# - 特に複数回nCrを算出する問題で有用。
#
# リンク
# - 
# 
# 計算量
# - O(factorial_max)
# 
# verify
# - https://atcoder.jp/contests/abc132/tasks/abc132_d
# ------------------------------------------------------------------------------
class Combination():
    def __init__(self, factorial_max: int, mod: int) -> None:
        """
        factorial_max = 7.3 * 10 ** 5 : Python limit (>2sec)
        factorial_max = 10 ** 6 : PyPy limit (=260 ~ 280msec)
        
        O(factorial_max)
        """
        self.fac = [1, 1]  # fac : 階乗(1!,2!,3!,...)
        self.factorial_max = factorial_max
        self.finv = [1, 1] # inv : 逆元(1,1/2,...1/N) -> inv[i] = pow(i, MOD - 2, MOD) # フェルマーの小定理より
        self.inv = [0, 1]  # finv: 階乗の逆元(1/1!, 1/2!, 1/3!...)
        self.mod = mod
        self._build()

    def _build(self):
        for i in range(2, self.factorial_max):
            self.fac.append(self.fac[i - 1] * i % self.mod)
            self.inv.append(self.mod - self.inv[self.mod % i] * (self.mod // i) % self.mod)
            self.finv.append(self.finv[i - 1] * self.inv[i] % self.mod)

    def nCr(self, n: int, r: int):
        """
        O(1)
        """
        if n < r: return 0
        if n < 0 or r < 0: return 0
        return self.fac[n] * (self.finv[r] * self.finv[n - r] % self.mod) % self.mod
        
    def nHr(self, n: int, r: int):
        """
        ◯◯◯◯|◯◯|◯ ← これ系の問題。
        * (n - 1) : 仕切り版の数
        * r : 分配する物自体の数
        
        * 区別のない r 個の物を n グループに分配する。
        eg.) 5個のボールを2個の箱に分配する分け方 : 2H5
        * n 種類の物から重複を許して r 個選択する。
        eg.) 3種類の果物から4個選ぶ取り方 : 3H4
        
        O(1)
        """
        return self.nCr(n - 1 + r, r)

# Usage
MOD = 10 ** 9 + 7
comb = Combination(5000, MOD)
# 特に複数回nCrを計算する場面で有用。
print([comb.nCr(10, i) for i in range(10)]) # [1, 10, 45, 120, 210, 252, 210, 120, 45, 10]
    