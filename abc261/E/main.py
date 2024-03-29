#!/usr/bin/env python3
import sys


def solve(N: int, C: int, T: "List[int]", A: "List[int]"):
    l = [0] * 30
    req = [[0 for _ in range(30)] for _ in range(3)]
    for i in range(30):
        if C >> i & 1:
            l[i] = 1
    for q in range(N):
        for i in range(30):
            if T[q] - 1 == 0:
                req[T[q] - 1][i] &= (A[q] >> i & 1)
            elif T[q] - 1 == 1:
                req[T[q] - 1][i] |= (A[q] >> i & 1)
            else:
                req[T[q] - 1][i] ^= (A[q] >> i & 1)
        for i in range(30):
            l[i] &= req[0][i]
            l[i] |= req[1][i]
            l[i] ^= req[2][i]
        print(l)


        
        
    print(l)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    T = [int()] * (N)  # type: "List[int]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        T[i] = int(next(tokens))
        A[i] = int(next(tokens))
    solve(N, C, T, A)

if __name__ == '__main__':
    main()
