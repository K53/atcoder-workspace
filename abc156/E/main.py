#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

class Combination():
    def __init__(self, factorial_max: int, mod: int) -> None:
        """
        factorial_max = 7.3 * 10 ** 5 : Python limit (>2sec)
        factorial_max = 10 ** 6 : PyPy limit (=260 ~ 280msec)
        
        O(factorial_max)
        """
        self.fac = [1, 1]  # fac : 階乗(1!,2!,3!,...)
        self.factorial_max = factorial_max + 1
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
        * n : 仕切り版の数 + 1
        * r : 分配する物(◯)自体の数
        
        * 区別のない r 個の物を n グループに分配する。
        eg.) 5個のボールを2個の箱に分配する分け方 : 2H5
        * n 種類の物から重複を許して r 個選択する。
        eg.) 3種類の果物から4個選ぶ取り方 : 3H4
        
        O(1)
        """
        return self.nCr(n - 1 + r, r)

def solve(n: int, k: int):
    k = min(k, n - 1)
    comb = Combination(2 * n + 1, MOD)
    ans = 0
    for i in range(k + 1): # ゼロ人の部屋がi個
        ans += (comb.nCr(n, i) * comb.nHr(n - i, i)) % MOD
        ans %= MOD
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(n, k)

if __name__ == '__main__':
    main()
