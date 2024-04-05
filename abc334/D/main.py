#!/usr/bin/env python3
from itertools import accumulate
import bisect

def main():
    N, Q = map(int, input().split())
    R = list(accumulate(sorted(list(map(int, input().split())))))
    for _ in range(Q):
        X = int(input())
        print(bisect.bisect_right(R, X))

    return

if __name__ == '__main__':
    main()
