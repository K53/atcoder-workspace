#!/usr/bin/env python3
import math

def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)

    if maxA in A[:(2 ** N // 2)]:
        print(A.index(max(A[(2 ** N // 2):])) + 1)
    else:
        print(A.index(max(A[:(2 ** N // 2)])) + 1)
    return

if __name__ == '__main__':
    main()
