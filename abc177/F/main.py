#!/usr/bin/env python3
import sys


def solve(H: int, W: int, A: "List[int]", B: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = [int()] * (H)  # type: "List[int]"
    B = [int()] * (H)  # type: "List[int]"
    for i in range(H):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(H, W, A, B)

if __name__ == '__main__':
    main()
