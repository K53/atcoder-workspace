#!/usr/bin/env python3
import sys

MOD = 10007  # type: int


def solve(L: int, A: int, B: int, M: int):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(L, A, B, M)

if __name__ == '__main__':
    main()
