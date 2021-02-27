#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", P: "List[int]", X: "List[int]"):
    ans = 10 ** 10
    for i in range(N):
        if X[i] - A[i] > 0:
            ans = min(ans, P[i])
    print( -1 if ans == 10 ** 10 else ans)

    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    X = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        P[i] = int(next(tokens))
        X[i] = int(next(tokens))
    solve(N, A, P, X)

if __name__ == '__main__':
    main()
