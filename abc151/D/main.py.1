#!/usr/bin/env python3
import sys

def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    INF = 10 ** 16
    from collections import deque
    def bfs(G, H, W, startY, startX) -> list:
        q = deque()
        dist = [[-INF] * W for _ in range(H)]
        q.append((startY, startX))
        dist[startY][startX] = 0
        while q:
            nowy, nowx = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != -INF or G[nexty][nextx] == "#":
                    continue
                q.append((nexty, nextx))
                dist[nexty][nextx] = dist[nowy][nowx] + 1
        # for i in range(H):
        #     for j in range(W):
        #         if dist[i][j] == INF:
        #             dist[i][j] = -1
        return dist
    ans = -INF
    for sy in range(H):
        for sx in range(W):
            if S[sy][sx] == "#":
                continue
            dist = bfs(S, H, W, sy, sx)
            m = max([max(dist[i]) for i in range(H)])
            ans = max(ans, m)
    print(ans)
    # dd = bfs(S, H, W, 0, 1)
    # for i in range(H):
    #     print(dd[i])
            




if __name__ == '__main__':
    main()
