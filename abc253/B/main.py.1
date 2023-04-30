#!/usr/bin/env python3
import sys
from collections import deque
def bfs(G, H, W, startY, startX) -> list:
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
            q.append((nexty, nextx))
            dist[nexty][nextx] = dist[nowy][nowx] + 1
    return dist

def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    # print(G)
    sg = []
    for hh in range(H):
        for ww in range(W):
            if G[hh][ww] == "o":
                sg.append((hh, ww))
    # print(sg)
    d = bfs(G, H, W, sg[0][0], sg[0][1])
    print(d[sg[1][0]][sg[1][1]])
    return


if __name__ == '__main__':
    main()
