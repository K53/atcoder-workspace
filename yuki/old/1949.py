#!/usr/bin/env python3
import sys
import heapq
INF = 10 ** 16

def main():
    H, W, Y, X = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(list(map(int, input().split())))
    hq = [(0, Y - 1, X - 1)]
    heapq.heapify(hq)
    seen = [[0] * W for _ in range(H)]
    seen[Y - 1][X - 1] = 1
    now = G[Y - 1][X - 1]
    G[Y - 1][X - 1] = 0
    while hq:
        cost, nowy, nowx = heapq.heappop(hq)
        if cost >= now:
            print("No")
            return
        now += cost
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nexty = nowy + dy
            nextx = nowx + dx
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or seen[nexty][nextx]:
                continue
            
            heapq.heappush(hq, (G[nexty][nextx], nexty, nextx))
            seen[nexty][nextx] = 1
        
    print("Yes")
    return


if __name__ == '__main__':
    main()