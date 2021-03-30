#!/usr/bin/env python3
import sys
import heapq

YES = "Yes"  # type: str
NO = "No"  # type: str

def main():
    N = int(input())
    BA = []
    heapq.heapify(BA)
    for _ in range(N):
        a, b = map(int, input().split())
        heapq.heappush(BA, (b, a))

    now = 0
    for _ in range(N):
        end, task = heapq.heappop(BA)
        if now + task > end:
            print(NO)
            return
        now += task
    print(YES)
    return

if __name__ == '__main__':
    main()
