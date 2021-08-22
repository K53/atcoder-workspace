#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int
INF = 10 ** 9

def main():
    H, W = map(int, input().split())
    field = []
    for _ in range(H):
        field.append(input())
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    for nowy in range(H):
        for nowx in range(W):
            for dx, dy in [(0, 1), (1, 0)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or field[nexty][nextx] == "#":
                    continue
                dp[nexty][nextx] += dp[nowy][nowx] % MOD
    print(dp[-1][-1] % MOD)
    return

if __name__ == '__main__':
    main()
