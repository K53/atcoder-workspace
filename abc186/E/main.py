#!/usr/bin/env python3
# 拡張ユークリッドの互除法
# ax + by = gcd(a, b) を満たす整数(a,b)の組を求める。
def ext_gcd(a: int, b: int):
    if a == 0: return (0, 1, b)
    else:
        (X, Y, g) = ext_gcd(b % a, a)
        return (Y - (b // a) * X, X, g)

def getInverse(A: int, mod: int):
    x, _, g = ext_gcd(A, mod)
    if g != 1: return -1 # no inverse exists
    return x % mod

import math
# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    T = int(input())
    for _ in range(T):
        N, S, K = map(int, input().split())
        g = math.gcd(math.gcd(N, S), K)
        N, X, K = N//g, (N - S)//g, K//g
        if math.gcd(K, N) != 1:
            print(-1)
        else:
            inv = getInverse(K, N)
            ans = (inv * X) % N
            print(ans)
    return        


if __name__ == '__main__':
    main()
