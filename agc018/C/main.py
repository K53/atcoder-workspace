#!/usr/bin/env python3
import sys


def solve(X: int, Y: int, Z: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    Z = int(next(tokens))  # type: int
    A = [int()] * (X + Y + Z)  # type: "List[int]"
    B = [int()] * (X + Y + Z)  # type: "List[int]"
    C = [int()] * (X + Y + Z)  # type: "List[int]"
    for i in range(X + Y + Z):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(X, Y, Z, A, B, C)

if __name__ == '__main__':
    main()
