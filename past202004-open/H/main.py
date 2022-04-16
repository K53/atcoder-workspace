#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    G = []
    for yy in range(N):
        l = input()
        if "S" in l:
            xx = l.index("S")
            sy, sx = yy, xx
        G.append(l)
    from collections import deque
    def bfs(G, H, W, startY, startX, dest) -> list:
        INF = 10 ** 16
        q = deque()
        dist = [[INF] * W for _ in range(H)]
        q.append((startY, startX))
        dist[startY][startX] = 0
        while q:
            nowy, nowx = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != INF:
                    continue
                if G[nexty][nextx] == dest:
                    return (nexty, nextx, dist[nowy][nowx] + 1)
                q.append((nexty, nextx))
                dist[nexty][nextx] = dist[nowy][nowx] + 1
        return (-1, -1, -1)

    ans = 0
    for dest in "123456789G":
        sy, sx, d = bfs(G, N, M, sy, sx, dest)
        print(sy, sx, d)
        if d == -1:
            print(-1)
            return
        ans += d
    print(ans)


if __name__ == '__main__':
    main()
