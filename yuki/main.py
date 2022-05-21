#!/usr/bin/env python3
import sys
# MOD = 998244353
MAX = 500
MOD = 1000000007  # type: int

fac, finv, inv = [1, 1], [1, 1], [0, 1]
# fac : 階乗(1,2,6,...)
# inv : 逆元(1,2,...N) -> inv[i] = pow(i, 10 ** 9 + 5, 10 ** 9 + 7)
# finv: 逆元(階乗の逆元 = 1の逆元, 2の逆元, 6の逆元)
def cmbInit():
    for i in range(2, MAX):
        fac.append(fac[i - 1] * i % MOD)
        inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
        finv.append(finv[i - 1] * inv[i] % MOD)

# 二項係数計算
def cmbMod(n: int, k: int):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    cmbInit()
    for i in range(N):
        ans += A[i] * cmbMod(N - 1, i)
        # print(A[i], cmbMod(N - 1, i))
        # print(ans)
        ans %= MOD
    print(ans)
    return

if __name__ == '__main__':
    main()