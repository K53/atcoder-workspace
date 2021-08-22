#!/usr/bin/env python3
import sys
import math

def main():
    N = int(input())
    p = list(map(float, input().split()))
    dp = [[0.0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1.0
    # i 枚まで振って、 j 枚が表である。
    for i in range(N):
        for j in range(N):
            dp[j][i + 1] += dp[j][i] * (1 - p[i])
            dp[j + 1][i + 1] += dp[j][i] * p[i]
    # for i in range(N + 1):
    #     print(dp[i])

    ans = 0
    for i in range(math.ceil(N / 2)):
        ans += dp[-1 - i][-1]

    print(ans)
if __name__ == '__main__':
    main()
