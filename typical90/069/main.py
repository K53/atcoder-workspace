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

def solve(N: int, K: int):
    if N == 1:
        print(K % MOD)
        return
    if N == 2:
        print((K * (K - 1)) % MOD)
        return

    print((K * (K - 1) * modpow(K - 2, N - 2)) % MOD)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
