#!/usr/bin/env python3
import queue
INF = 10 ** 9
def bfs(field: "List[Lsit[]]", H: int, W: int, y: int, x: int) -> list:
    q = queue.Queue()
    dist = []
    for _ in range(H):
        dist.append([-INF] * W)
    q.put((x, y))
    dist[y][x] = 0
    while not q.empty():
        now_x, now_y= q.get()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = now_x + dx, now_y + dy
            if next_y < 0 or next_y >= H or next_x < 0 or next_x >= W or field[next_y][next_x] == "#" or dist[next_y][next_x] != -INF:
                continue
            q.put((next_x, next_y))
            dist[next_y][next_x] = dist[now_y][now_x] + 1
    return dist

def main():
    H, W = map(int, input().split())
    field = []
    for _ in range(H):
        field.append(input())
    ans = 0
    for hh in range(H):
        for ww in range(W):
            if field[hh][ww] == "#":
                continue
            dist = bfs(field, H, W, hh, ww)
            for d in dist:
                ans = max(ans, max(d))
    print(ans)

if __name__ == '__main__':
    main()
