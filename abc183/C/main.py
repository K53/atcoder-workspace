#!/usr/bin/env python3
import sys
import itertools

def main():
    N, K = map(int, input().split())
    T = []
    n = []
    for i in range(N):
        T.append(list(map(int, input().split())))
        n.append(i)

    ans = 0
    for way in list(itertools.permutations(n[1:])):
        w = list(way)
        w.append(0)
        now = 0
        count = 0
        for i in range(N):
            next = w[i]
            count += T[now][next]
            now = next
        if count == K:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
