#!/usr/bin/env python3
from collections import deque

def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(list(input()))
    
    def bfs(startY, startX) -> list:
        # ゴールやスタートを任意に設定できる問題では開始点が壁であるケースに注意!!!!
        INF = 10 ** 16
        q = deque()
        # dist = [[INF] * W for _ in range(H)]
        q.append((startY, startX))
        # dist[startY][startX] = 0
        count = 0
        while q:
            nowy, nowx = q.popleft()
            for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or G[nexty][nextx] == ".":
                    continue
                q.append((nexty, nextx))
                # dist[nexty][nextx] = dist[nowy][nowx] + 1
                G[nexty][nextx] = "."
                count += 1
        return (count - 1) // 4
        
    ans = [0] * min(H, W)
    for hh in range(H):
        for ww in range(W):
            if G[hh][ww] == "#":
                k = bfs(hh, ww)
                ans[k - 1] += 1
    print(*ans, sep=" ")
    return

if __name__ == '__main__':
    main()
