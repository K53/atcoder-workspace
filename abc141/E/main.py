#!/usr/bin/env python3
import sys
import random
INT_MAX_VALUE = 2147483647

# https://qiita.com/keymoon/items/11fac5627672a6d6a9f6

mersenne_numbers = [2, 3, 5, 7, 13, 17, 19, 31] # < 32

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


def solve(N: int, S: str):
    curMaxLength = 0
    rlh1 = RollingHash(S, 31)
    rlh2 = RollingHash(S, 17)
    for i in range(len(S)):
        for j in range(i, len(S)):
            while (curMaxLength < j - i and \
                j + curMaxLength < N and \
                rlh1.getHash(i, i + curMaxLength + 1) == rlh1.getHash(j, j + curMaxLength + 1) and \
                rlh2.getHash(i, i + curMaxLength + 1) == rlh2.getHash(j, j + curMaxLength + 1)):
                curMaxLength += 1
    print(curMaxLength)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
