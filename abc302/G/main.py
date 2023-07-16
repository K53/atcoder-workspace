#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    SA = sorted(A)
    d = {
        1: set(),
        2: set(),
        3: set(),
        4: set()
    }
    need = set()
    for i in range(N):
        if SA[i] != A[i]:
            need.add(i)
    
    for i in need:
        for cv in d[SA[i]]:
            if A[i] == A[cv]:
                A[i], A[cv] = A[cv], A[i]

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()