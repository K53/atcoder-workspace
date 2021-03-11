#!/usr/bin/env python3
import sys
MOD = 1000000007  # type: int

def main():
    N = int(input())
    pq = (10 ** N - 9 ** N) % MOD
    rest = 8 ** N % MOD
    u = 10 ** N % MOD
    ans = pq * 2 + rest - u
    print(ans % MOD)

if __name__ == '__main__':
    main()
