#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    p = list(map(float, input().split()))
    dp = []
    for _ in range(0, N + 1):
        dp.append([0.0] * (N + 1))
    
    dp[1][0] = 1 - p[0]
    dp[1][1] = p[0]

    for i in range(2, N + 1):
        for j in range(0, i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] * (1 - p[i - 1])
            else:
                dp[i][j] = dp[i - 1][j - 1] * p[i - 1] + dp[i - 1][j] * (1 - p[i - 1])
 
    res = 0
    for j in range(0, N + 1):
        if j < N / 2:
            continue
        res += dp[N][j]
    print(res)

if __name__ == '__main__':
    main()
