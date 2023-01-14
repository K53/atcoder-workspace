#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str

INF = 10 ** 16
from collections import deque
def bfs(G, H, W, startY, startX) -> list:
    q = deque()
    dist = [[INF] * W for _ in range(H)]
    q.append((startY, startX))
    dist[startY][startX] = 0
    while q:
        nowy, nowx = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nexty = nowy + dy
            nextx = nowx + dx
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != INF or G[nexty][nextx] != ".":
                continue
            q.append((nexty, nextx))
            dist[nexty][nextx] = dist[nowy][nowx] + 1
    return dist


def main():
    H, W = map(int, input().split())
    G = []
    for i in range(H):
        l = input()
        G.append(l)
        if "S" in l:
            hh = i
            ww = l.index("S")
    # print(hh, ww, G[hh][ww])
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        srcy = hh + dy
        srcx = ww + dx
        if srcy < 0 or srcx < 0 or srcy >= H or srcx >= W or G[srcy][srcx] != ".":
            continue
        d = bfs(G, H, W, srcy, srcx)
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            desty = hh + dy
            destx = ww + dx
            if desty < 0 or destx < 0 or desty >= H or destx >= W or (desty == srcy and destx == srcx):
                continue
            if d[desty][destx] != INF:
                print(YES)
                return
    print(NO)
if __name__ == '__main__':
    main()
