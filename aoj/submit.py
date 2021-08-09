#!/usr/bin/env python3
import sys

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_A&lang=jp

def main():
    N, M = map(int, input().split())
    INF = 10 ** 9
    cc = list(map(int, input().split()))
    dp = [[INF] * 50001 for _ in range(M + 1)]
    dp[0][0] = 0
    for i in range(1, M + 1):
        for j in range(50001):
            if j - cc[i - 1] >= 0:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - cc[i - 1]] + 1)
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[-1][N])
    return

if __name__ == '__main__':
    main()
