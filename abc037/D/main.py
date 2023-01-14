import sys
sys.setrecursionlimit(10**6)
from functools import lru_cache

H, W = map(int, input().split())
G = [list(map(int, input().split())) for hh in range(H)]
MOD = 1000000007  # type: int

@lru_cache(maxsize=7000)
def dfs(now_y,now_x):
    count = 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x = now_x + dx
        next_y = now_y + dy
        if 0 <= next_x < W and 0 <= next_y < H:
            if G[now_y][now_x] > G[next_y][next_x]:
                count += dfs(next_y, next_x)
                count %= MOD
    return count

ans = 0
for hh in range(H):
    for ww in range(W):
        ans += dfs(hh, ww)
        ans %= MOD

print(ans)