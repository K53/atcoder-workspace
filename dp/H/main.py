#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int
INF = 10 ** 9

def main():
    H, W = map(int, input().split())
    field = []
    for _ in range(H):
        field.append(list(input()))

    dp = []
    for _ in range(H):
        dp.append([INF] * W)
    
    isBlockFound = False
    for w in range(W):
        if isBlockFound or field[0][w] == "#":
            dp[0][w] = 0
            isBlockFound = True
        else:
            dp[0][w] = 1

    isBlockFound = False
    for h in range(H):
        if isBlockFound or field[h][0] == "#":
            dp[h][0] = 0
            isBlockFound = True
        else:
            dp[h][0] = 1
    
    for h in range(1, H):
        for w in range(1, W):
            dp[h][w] = 0 if field[h][w] == "#" else ((dp[h - 1][w] + dp[h][w - 1]) % MOD)

    print(dp[-1][-1])
    return


if __name__ == '__main__':
    main()
