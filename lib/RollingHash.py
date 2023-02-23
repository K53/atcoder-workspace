import sys
import random
INT_MAX_VALUE = 2147483647

# https://qiita.com/keymoon/items/11fac5627672a6d6a9f6

mersenne_numbers = [2, 3, 5, 7, 13, 17, 19, 31] # < 32

# 複数に対応しないと S T みたいな

class RollingHash():
    def __init__(self, s: str, mersenne_exp) -> None:
        self.mersenne_exp = mersenne_exp
        self.mask_head = (1 << (self.mersenne_exp // 2)) - 1
        self.mask_tail = (1 << (self.mersenne_exp // 2 + 1)) - 1
        self.MOD = (1 << self.mersenne_exp) - 1
        self.POSITIVIZER = self.MOD * ((1 << 3) - 1)
        self.base = random.randint(129, self.MOD - 1) # 原始根でないと衝突するかも？
        self.powMemo = [1]
        for i in range(len(s) + 1):
            self.powMemo.append(self._calcMod(self._mul(self.powMemo[-1], self.base)))
        self.hash = [0]
        for i in range(len(s)):
            self.hash.append(self._calcMod(self._mul(self.hash[-1], self.base) + ord(s[i])))

    def getHash(self, l:int, r: int) -> int:
        return self._calcMod(self.hash[r] + self.POSITIVIZER - self._mul(self.hash[l], self.powMemo[r - l]))

    def _mul(self, a: int, b: int) -> int:
        """
        a * b % MODの高速化
        pythonは確か2^30？32？進数管理してるので超えると遅くなったか何かのはず
        https://qiita.com/keymoon/items/11fac5627672a6d6a9f6
        """
        au = a >> (self.mersenne_exp // 2 + 1)
        ad = a & self.mask_tail
        bu = b >> (self.mersenne_exp // 2 + 1)
        bd = b & self.mask_tail
        mid = ad * bu + au * bd
        midu = mid >> (self.mersenne_exp // 2)
        midd = mid & self.mask_head
        return self._calcMod(au * bu * 2 + midu + (midd << (self.mersenne_exp // 2 + 1)) + ad * bd)

    def _calcMod(self, val: int) -> int:
        """
        return val % MOD に等しい。
        """
        val = (val & self.MOD) + (val >> self.mersenne_exp)
        if (val > self.MOD):
            val -= self.MOD
        return val

# Usage
S = "abcdef"
T = "xxcdxx"
rlh1s = RollingHash(S, 31)
rlh2s = RollingHash(S, 17)
rlh1t = RollingHash(T, 31)
rlh2t = RollingHash(T, 17)
if rlh1s.getHash(2, 4) == rlh1t.getHash(2, 4) and \
    rlh2s.getHash(2, 4) == rlh2t.getHash(2, 4):
    print("same!")
else:
    print("NO")