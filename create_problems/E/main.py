#!/usr/bin/env python3
import sys
from collections import deque
def bfs01(G, H, W, startY, startX) -> list:
    # ゴールやスタートを任意に設定できる問題では開始点が壁であるケースに注意!!!!
    INF = 10 ** 16
    qs = [deque() for _ in range(10)]
    qs[0].append((startY, startX))
    count = [[INF] * W for _ in range(H)]
    count[startY][startX] = 0
    while True:
        for q in qs:
            if len(q) > 0:
                nowy, nowx = q.popleft()
                break
        else:
            break
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nexty = nowy + dy
            nextx = nowx + dx
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W:
                continue
            if count[nexty][nextx] > count[nowy][nowx]:
                count[nexty][nextx] = count[nowy][nowx] + int(G[nexty][nextx])
                qs[int(G[nexty][nextx])].append((nexty, nextx))
    return count

#   222
#  22122
#  21T12
#  22122
#   222
    
def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    d = bfs01(G, H, W, 0, 0)
    print(d[-1][-1])
    return


if __name__ == '__main__':
    main()
