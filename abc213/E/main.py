#!/usr/bin/env python3
from collections import deque
def bfs01(G, H, W, startY, startX) -> list:
    # ゴールやスタートを任意に設定できる問題では開始点が壁であるケースに注意!!!!
    INF = 10 ** 16
    q = deque()
    q.append((startY, startX))
    count = [[INF] * W for _ in range(H)]
    count[startY][startX] = 0
    while q:
        nowy, nowx = q.popleft()
        for dx in range(-2, 2 + 1):
            for dy in range(-2, 2 + 1):
                nexty = nowy + dy
                nextx = nowx + dx
                if (dx, dy) in [(0, 0), (-2, 2), (-2, -2), (2, 2), (2, -2)]:
                    continue
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W:
                    continue
                # 特殊な移動をしない
                if (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if G[nexty][nextx] == "#":
                        continue
                    if count[nexty][nextx] > count[nowy][nowx]:
                        count[nexty][nextx] = count[nowy][nowx]
                        q.appendleft((nexty, nextx))
                # 特殊な移動をする
                else:  
                    if count[nexty][nextx] > count[nowy][nowx] + 1:
                        count[nexty][nextx] = count[nowy][nowx] + 1
                        q.append((nexty, nextx))
    return count

def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]
    count = bfs01(G, H, W, 0, 0)
    print(count[-1][-1])


if __name__ == '__main__':
    main()
