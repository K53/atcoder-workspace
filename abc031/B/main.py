#!/usr/bin/env python3
import sys


def solve(L: int, H: int, N: int, A: "List[int]"):
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    L = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(L, H, N, A)

if __name__ == '__main__':
    main()
