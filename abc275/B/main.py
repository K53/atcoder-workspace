#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(A: int, B: int, C: int, D: int, E: int, F: int):
    aa = A % MOD
    bb = B % MOD
    cc = C % MOD
    dd = D % MOD
    ee = E % MOD
    ff = F % MOD
    ans = ((((aa * bb) % MOD) * cc) % MOD - (((dd * ee) % MOD) * ff) % MOD) % MOD
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    F = int(next(tokens))  # type: int
    solve(A, B, C, D, E, F)

if __name__ == '__main__':
    main()