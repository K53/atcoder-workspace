#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", S: "List[int]", T: "List[int]"):
    for i in range(N - 1):
        count = A[i] // S[i]
        A[i + 1] += count * T[i]
    print(A[-1])
    return


# Generated by 2.13.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    S = [int()] * (N - 1)  # type: "List[int]"
    T = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
    solve(N, A, S, T)

if __name__ == '__main__':
    main()