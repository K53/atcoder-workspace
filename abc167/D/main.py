#!/usr/bin/env python3
import sys
import math

def main():
    N, K = map(int, input().split())
    A = list(map(lambda i: int(i) - 1, input().split()))
    d = [[None] * N for _ in range(100)]    # log2(10^18)あれば足りる
    d[0] = A
    # print(d[0])
    for i in range(1, 100):
        for j in range(N):
            d[i][j] = d[i - 1][d[i - 1][j]]
        # print(d[i])
    now = 0
    for i in range(100):
        if K >> i & 1:
            now = d[i][now]
    print(now + 1)


if __name__ == '__main__':
    main()
