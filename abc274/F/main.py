#!/usr/bin/env python3
import sys


def solve(N: int, A: int, W: "List[int]", X: "List[int]", V: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    W = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    V = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        W[i] = int(next(tokens))
        X[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, A, W, X, V)

if __name__ == '__main__':
    main()
