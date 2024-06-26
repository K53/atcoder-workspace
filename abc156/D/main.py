#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int

def cmb(n: int, r: int, mod: int= 1):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2, r + 1):                    # p番目について、
        pivot = denominator[p - 1]               # pivotで約分を試みる。
        if pivot > 1:                            # ただし、pivotが1、すなわちすでに割り尽くされているならp番目は飛ばす。
            offset = (n - r) % p
            for k in range(p - 1, r, p):            # p番目を約分できるということはp番目からpの倍数番目も約分可能なので実施する。
                numerator[k - offset] //= pivot
                denominator[k] //= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
            result %= mod
    return result

def solve(n: int, a: int, b: int):
    print((pow(2, n, MOD) - 1 - cmb(n, a, MOD) - cmb(n, b, MOD)) % MOD)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(n, a, b)

if __name__ == '__main__':
    main()
