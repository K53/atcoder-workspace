#!/usr/bin/env python3
import sys

def main():
    N, M = map(int, input().split())
    INF = 10 ** 18
    dp = [[-INF for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    l = sorted([tuple(map(int, input().split())) for _ in range(N)], reverse=True)
    ans = 0
    for i in range(N):
        v, w = l[i]
        for j in range(M):
            if dp[i][j] == -INF:
                continue
            # 選ばない
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            # 選ぶ
            if j + w < M + 1 and dp[i + 1][j + w] < dp[i][j] + v:
                dp[i + 1][j + w] = dp[i][j] + v
                ans = max(ans, v * dp[i + 1][j + w])
    print(ans)

    return

if __name__ == '__main__':
    main()