#!/usr/bin/env python3
import sys


def solve(D: int, L: int, N: int, C: "List[int]", K: "List[int]", F: "List[int]", T: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(D)]  # type: "List[int]"
    K = [int()] * (N)  # type: "List[int]"
    F = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        K[i] = int(next(tokens))
        F[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(D, L, N, C, K, F, T)

if __name__ == '__main__':
    main()
