#!/usr/bin/env python3
import sys
MOD = 1000000007  # type: int

def modpow(n: int, a: int, mod: int = MOD) -> int:
    res = 1
    while a > 0:
        if a & 1:
            res = res * n % mod
        n = n * n % mod
        a >>= 1
    return res

def main():
    N = int(input())
    print((modpow(10, N) - modpow(9, N) * 2 + modpow(8, N)) % MOD)
    

if __name__ == '__main__':
    main()
