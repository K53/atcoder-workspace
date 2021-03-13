#!/usr/bin/env python3
import sys


def main():
    N = int(input())
    A = list(map(lambda i: int(i) - 1, input().split()))
    ans = [0] * N
    for a in A:
        ans[a] += 1
    print(*ans, sep="\n")
    return

if __name__ == '__main__':
    main()
