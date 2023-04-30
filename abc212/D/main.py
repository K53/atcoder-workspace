#!/usr/bin/env python3
import heapq

def main():
    Q = int(input())
    q = []
    offset = 0
    heapq.heapify(q)
    for _ in range(Q):
        t, *arg = map(int, input().split())
        if t == 1:
            num = arg[0] - offset
            heapq.heappush(q, num)
        elif t == 2:
            offset += arg[0]
        else:
            num = heapq.heappop(q)
            print(num + offset)
    return

if __name__ == '__main__':
    main()
