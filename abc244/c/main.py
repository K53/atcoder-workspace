#!/usr/bin/env python3
import sys


def main():
    N = int(input())
    S = [0] + [1] * (2 * N + 1)
    for i in range(N + 1):
        for k in range(2 * N + 2):
            if S[k]:
                S[k] = 0
                print(k)
                break
        y = int(input())
        S[y] = 0

if __name__ == '__main__':
    main()
