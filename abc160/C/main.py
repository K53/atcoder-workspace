#!/usr/bin/env python3
import sys


def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    A.append(K + A[0])
    distance = []
    for i in range(N):
        distance.append(A[i + 1] - A[i])
    print(K - max(distance))

if __name__ == '__main__':
    main()
