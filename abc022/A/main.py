#!/usr/bin/env python3
import sys


def solve(N: int, S: int, T: int, W: int, A: "List[int]"):
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N - 2 + 1)]  # type: "List[int]"
    solve(N, S, T, W, A)

if __name__ == '__main__':
    main()
