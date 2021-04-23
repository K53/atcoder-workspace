#!/usr/bin/env python3
import sys
import heapq

def main():
    cb = []
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    heapq.heapify(A)
    for _ in range(M):
        b, c = map(int, input().split())
        cb.append((c, b))
    cb.sort(reverse=True)
    ans = 0
    for c, b in cb:
        for _ in range(b):
            if len(A) == 0:
                print(ans)
                return
            next = heapq.heappop(A)
            if next >= c:
                print(ans + next + sum(A))
                return
            ans += c
    print(ans + sum(A))

if __name__ == '__main__':
    main()

