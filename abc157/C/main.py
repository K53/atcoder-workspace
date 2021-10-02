#!/usr/bin/env python3
import sys


def main():
    N, M = map(int, input().split())
    sc = set()
    for _ in range(M):
        s, c = map(int, input().split())
        sc.add((s, c))
    l, r = 0, 0
    if N == 1:
        l, r = 0, 10
    else:
        l, r = 10 ** (N - 1), 10 ** N
    for i in range(l, r):
        ss = str(i)
        for s, c in sc:
            if s > N or int(ss[s - 1]) != c:
                break
        else:
            print(i)
            return
    print(-1)
    return


if __name__ == '__main__':
    main()
