#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(0, N - 1):
        if A[i] <= A[i + 1]:
            continue
        else:
            ans += A[i] - A[i + 1]
            A[i + 1] = A[i]
    print(ans)

if __name__ == '__main__':
    main()
