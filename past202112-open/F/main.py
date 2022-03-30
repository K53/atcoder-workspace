#!/usr/bin/env python3
import sys


def main():
    A, B = map(int, input().split())
    move = []
    for i in range(3):
        ss = input()
        for j in range(3):
            if ss[j] == "#":
                move.append((j - 1, i - 1))

    from collections import deque
    def bfs(H, W, startY, startX) -> list:
        q = deque()
        dist = [[0] * W for _ in range(H)]
        q.append((startY, startX))
        dist[startY][startX] = 1
        while q:
            nowy, nowx = q.popleft()
            for dx, dy in move:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != 0:
                    continue
                q.append((nexty, nextx))
                dist[nexty][nextx] = 1
        return dist
    
    d = bfs(9, 9, A - 1, B - 1)
    ans = 0
    for dd in d:
        # print(dd)
        ans += sum(dd)
    print(ans)
    return
if __name__ == '__main__':
    main()
