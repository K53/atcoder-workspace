#!/usr/bin/env python3
import sys


def solve(A: int, R: int, N: int):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(A, R, N)

if __name__ == '__main__':
    main()
