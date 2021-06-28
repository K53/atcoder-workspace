#!/usr/bin/env python3
import copy

def main():
    H, W = map(int, input().split())
    field = []
    visited = [[0] * W for _ in range(H)]
    for _ in range(H):
        field.append(input())
    def dfs(v, now, count):
        maxCount = 0
        visited = copy.deepcopy(v)
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            # print(now, count)
            next = (now[0] + dy, now[1] + dx)
            if now[0] + dy < 0 or now[0] + dy >= H or now[1] + dx < 0 or now[1] + dx >= W or field[now[0] + dy][now[1] + dx] == "#":
                continue
            if visited[next[0]][next[1]] == -1 and count >= 3:
                return count + 1
            if visited[now[0] + dy][now[1] + dx] == 1:
                continue
            visited[now[0] + dy][now[1] + dx] = 1
            maxCount = max(maxCount, dfs(visited, next, count + 1)) 
        return maxCount
    ans = 0
    for y in range(H):
        for x in range(W):
            v = copy.deepcopy(visited)
            v[y][x] = -1
            ans = max(ans, dfs(v, (y, x), 0))
    print(-1 if ans == 0 else ans)

if __name__ == '__main__':
    main()
