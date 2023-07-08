#!/usr/bin/env python3

from collections import deque
INF = 10 ** 16
def bfs(G, H, W, startY, startX) -> list:
    # ゴールやスタートを任意に設定できる問題では開始点が壁であるケースに注意!!!!
    q = deque()
    dist = [[INF] * W for _ in range(H)]
    q.append((startY, startX))
    dist[startY][startX] = 0
    while q:
        nowy, nowx = q.popleft()
        for dx, dy in [(0, 1), (1, 0)]:
            nexty = nowy + dy
            nextx = nowx + dx
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != INF or G[nexty][nextx] == "#":
                continue
            q.append((nexty, nextx))
            dist[nexty][nextx] = dist[nowy][nowx] + 1
    return dist

def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    d = bfs(G, H, W, 0, 0)
    ans = 0
    for hh in range(H):
        for ww in range(W):
            if d[hh][ww] == INF:
                continue
            ans = max(ans, d[hh][ww])
    print(ans + 1)
    return

if __name__ == '__main__':
    main()
