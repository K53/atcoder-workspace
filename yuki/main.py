#!/usr/bin/env python3
from bisect import bisect_left
from itertools import accumulate
import sys

MOD = 998244353

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = []
    for aa in A:
        for i in range(1, aa + 1):
            B.append(i)
    SB = list(accumulate(B))
    m = len(SB)
    # print(SB)
    for _ in range(Q):
        S = int(input())
        if S == SB[-1]:
            print(m)
            continue
        ans = bisect_left(SB, S)
        print(ans + 1 if ans < m else -1)
    return

if __name__ == '__main__':
    main()

