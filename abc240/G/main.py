#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, X: int, Y: int, Z: int):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    solve(N, X, Y, Z)

if __name__ == '__main__':
    main()
