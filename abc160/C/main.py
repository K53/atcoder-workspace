#!/usr/bin/env python3
import sys


def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(A[0] + K)
    d = []
    for i in range(N):
        d.append(A[i + 1] - A[i])
    print(sum(d) - max(d))
    return



if __name__ == '__main__':
    main()
