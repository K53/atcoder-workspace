#!/usr/bin/env python3
import sys


def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    way = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        way[A - 1].append(H[B - 1])
        way[B - 1].append(H[A - 1])
    ans = 0
    for i in range(N):
        if len(way[i]) == 0:
            ans += 1
            continue
        if max(way[i]) < H[i]:
            ans += 1
    print(ans)



if __name__ == '__main__':
    main()
