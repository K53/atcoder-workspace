#!/usr/bin/env python3
import sys
sys.setrecursionlimit(500 * 500)

YES = "Yes"  # type: str
NO = "No"  # type: str

H, W = 0, 0
field = []
dist = []  

def dfs(x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < W and 0 <= next_y < H and field[next_y][next_x] != "#" and dist[next_y][next_x] == -1:
            dist[next_y][next_x] = dist[y][x] + 1
            if field[next_y][next_x] == "g"or dfs(next_x, next_y):
                return True
    return False

def main():
    global H, W
    H, W = map(int, input().split())
    for _ in range(H):
        field.append(input())
        dist.append([-1] * W)

    for h in range(H):
        for w in range(W):
            if field[h][w] == "s":
                print(YES if dfs(w, h) else NO)
                return

if __name__ == '__main__':
    main()
