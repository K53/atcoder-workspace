#!/usr/bin/env python3
import queue

def main():
    q = queue.Queue()
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]
    dist = []
    ans = -1
    for sy in range(H):
        for sx in range(W):
            if field[sy][sx] == "#":
                continue
            dist = [[-1] * W for _ in range(H)]
            q.put((sx, sy))
            dist[sy][sx] = 0
            while not q.empty():
                x, y = q.get()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < W and 0 <= next_y < H and field[next_y][next_x] != "#" and dist[next_y][next_x] == -1:                        
                        q.put((next_x, next_y))
                        dist[next_y][next_x] = dist[y][x] + 1
            for d in dist:
                ans = max(ans, max(d))
    print(ans)

if __name__ == '__main__':
    main()
