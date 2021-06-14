#!/usr/bin/env python3
import sys
from itertools import combinations

def solve(N: int, P: int, Q: int, A: "List[int]"):
    count = 0
    for a1 in range(0, N - 4):
        for a2 in range(a1 + 1, N - 3):
            for a3 in range(a2 + 1, N - 2):
                for a4 in range(a3 + 1, N - 1):
                    for a5 in range(a4 + 1, N):
                        if ((A[a1] % P ) * (A[a2] % P) * (A[a3] % P) * (A[a4] % P) * (A[a5] % P)) % P == Q:
                            # print(A[a1] % P + A[a2] % P + A[a3] % P + A[a4] % P + A[a5] % P)
                            count += 1
    print(count)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, P, Q, A)

if __name__ == '__main__':
    main()
