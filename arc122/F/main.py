#!/usr/bin/env python3
import sys


def solve(N: int, M: int, K: int, RX: "List[int]", RY: "List[int]", BX: "List[int]", BY: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    RX = [int()] * (N)  # type: "List[int]"
    RY = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        RX[i] = int(next(tokens))
        RY[i] = int(next(tokens))
    BX = [int()] * (M)  # type: "List[int]"
    BY = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        BX[i] = int(next(tokens))
        BY[i] = int(next(tokens))
    solve(N, M, K, RX, RY, BX, BY)

if __name__ == '__main__':
    main()
