#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

def main():
    while True:
        W, H = map(int, sys.stdin.readline().split())
        if H == W == 0:
            return
        field = []
        seen = []
        for _ in range(H):
            field.append(list(map(int, sys.stdin.readline().split())))
            seen.append([False] * W)
        def dfs(y, x):
            seen[y][x] = True
            # 次の探索(分岐)
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                next_y = y + dy
                next_x = x + dx
                # 探索しない条件を切り落とし
                if next_x < 0 or next_y < 0 or next_x >= W or next_y >= H or field[next_y][next_x] == 0 or seen[next_y][next_x]:
                    continue
                dfs(next_y, next_x)
            return
        ans = 0
        for yy in range(H):
            for xx in range(W):
                if seen[yy][xx] or field[yy][xx] == 0:
                    continue
                dfs(yy, xx)
                ans += 1
        print(ans)
    return

if __name__ == '__main__':
    main()