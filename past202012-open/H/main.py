#!/usr/bin/env python3
from collections import deque

def main():
    H, W = map(int, input().split())
    r, c = map(int, input().split())
    f = []
    dist = []
    for _ in range(H):
        l = input()
        f.append(l)
        tmp = []
        for ww in range(W):
            tmp.append("#" if l[ww] == "#" else "x")
        dist.append(tmp) 

    # for i in range(H):
    #     print(*dist[i], sep="")

    def bfs(edges, H, W, startY, startX) -> list:
        q = deque()
        # dist = [["x"] * W for _ in range(H)]
        q.append((startY, startX))
        dist[startY][startX] = "o"
        while q:
            nowy, nowx = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != "x":
                    continue
                if edges[nexty][nextx] == "#":
                    dist[nexty][nextx] = "#"
                    continue
                if dx == 0 and dy == -1 and not edges[nexty][nextx] in "v.":
                    continue
                if dx == 1 and dy == 0 and not edges[nexty][nextx] in "<.":
                    continue
                if dx == -1 and dy == 0 and not edges[nexty][nextx] in ">.":
                    continue
                if dx == 0 and dy == 1 and not edges[nexty][nextx] in "^.":
                    continue
                q.append((nexty, nextx))
                dist[nexty][nextx] = "o"
        return dist

    
    d = bfs(f, H, W, r - 1, c - 1)
    for i in range(H):
        print(*d[i], sep="")
    

if __name__ == '__main__':
    main()
