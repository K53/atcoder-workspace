#!/usr/bin/env python3
import sys

INF = 10 ** 9

def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = INF
    for p in range(1, 101):
        s = 0
        for x in X:
            s += (x - p) ** 2
        # print(s)
        ans = min(ans, s)
    print(ans)


if __name__ == '__main__':
    main()
