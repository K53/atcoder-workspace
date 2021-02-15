#!/usr/bin/env python3
import queue

def main():
    q = queue.Queue()
    H, W = map(int, input().split())
    sy, sx = map(lambda n: int(n) - 1, input().split())
    gy, gx = map(lambda n: int(n) - 1, input().split())
    field = []
    dist = []                                        # スタートから何歩で移動できるか(数値) 兼 既に訪問したか(-1 or not)
    for _ in range(H):
        field.append(input())
        dist.append([-1] * W)
    q.put((sx, sy))
    dist[sy][sx] = 0
    while not q.empty():
        x, y = q.get()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = x + dx, y + dy
            if field[next_y][next_x] == "#" or dist[next_y][next_x] != -1:
                continue
            q.put((next_x, next_y))
            dist[next_y][next_x] = dist[y][x] + 1
    print(dist[gy][gx])

if __name__ == '__main__':
    main()
