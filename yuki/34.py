#!/usr/bin/env python3
import sys
from collections import deque
MOD = 998244353

input = sys.stdin.readline

powerMax = 99 * 2 * 9
INF = 10 ** 16

def main():
    N, V, Sx, Sy, Gx, Gy = map(int, input().split())
    if V > (abs(Sx-Gx) + abs(Sy-Gy)) * 9:
        print(abs(Sx-Gx) + abs(Sy-Gy))
        return
    V = min(V, powerMax)
    Grid = [list(map(int, input().split())) for _ in range(N)]

    def bfs(G, H, W, startY, startX, goalY, goalX, power_init) -> list:
        q = deque()
        dist = [[[INF] * (powerMax + 1) for _ in range(W)] for _ in range(H)]
        q.append((startY, startX, power_init))
        dist[startY][startX][power_init] = 0
        while q:
            nowY, nowX, now_power = q.popleft()
            if nowY == goalY and nowX == goalX:
                return dist[nowY][nowX][now_power]
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexty = nowY + dy
                nextx = nowX + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W:
                    continue
                next_power = now_power - G[nexty][nextx]
                if next_power <= 0 or dist[nexty][nextx][next_power] != INF:
                    continue
                q.append((nexty, nextx, next_power))
                dist[nexty][nextx][next_power] = dist[nowY][nowX][now_power] + 1
        return -1
    
    print(bfs(Grid, N, N, Sy - 1, Sx - 1, Gy - 1, Gx - 1, V))
    return

if __name__ == '__main__':
    main()