#!/usr/bin/env python3
import sys


def solve(N: int, K: int, Q: int, A: "List[int]", L: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    L = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, K, Q, A, L)

if __name__ == '__main__':
    main()
