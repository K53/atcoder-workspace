#!/usr/bin/env python3

def main():
    H, W = map(int, input().split())
    Cy, Cx = map(lambda i : int(i) - 1, input().split())
    Dy, Dx = map(lambda i : int(i) - 1, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    from collections import deque
    INF = 10 ** 9
    def bfs(edges, H, W, startY, startX) -> list:
        q = deque()
        dist = [[INF] * W for _ in range(H)]
        q.append((startY, startX))
        dist[startY][startX] = 0
        while q:
            # for i in range(len(dist)):
            #     print(dist[i])
            # print("------")
            nowy, nowx = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or edges[nexty][nextx] == "#" or dist[nexty][nextx] <= dist[nowy][nowx]:
                    continue
                q.appendleft((nexty, nextx))
                dist[nexty][nextx] = dist[nowy][nowx]
            for dx, dy in [(-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2), (-2, 1), (-1, 1), (1, 1), (2, 1), (-2, 0), (2, 0), (-2, -1), (-1, -1), (1, -1), (2, -1), (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or edges[nexty][nextx] == "#" or dist[nexty][nextx] < dist[nowy][nowx] + 1:
                    continue
                q.append((nexty, nextx))
                dist[nexty][nextx] = dist[nowy][nowx] + 1
        return dist
    d = bfs(G, H, W, Cy, Cx)
    # for i in range(len(d)):
    #     print(d[i])
    ans = d[Dy][Dx]
    print(-1 if ans == INF else ans)

if __name__ == '__main__':
    main()


