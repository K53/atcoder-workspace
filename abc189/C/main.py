#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    # for l in range(N):
    #     for r in range(l, N):
    #         ans = max(ans, min(A[l:r+1]) * (r - l + 1))
    for l in range(N):
        minOrange = A[l]
        for r in range(l, N):
            minOrange = min(minOrange, A[r])
            ans = max(ans, minOrange * (r - l + 1))
    print(ans)
    return

if __name__ == '__main__':
    main()

