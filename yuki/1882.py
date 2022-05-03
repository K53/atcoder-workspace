#!/usr/bin/env python3
from bisect import bisect_left
import sys

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for aa in A:
        b = K * 2 / aa
        res = N - bisect_left(A, b)
        ans += res
    print(ans)
    return


if __name__ == '__main__':
    main()
