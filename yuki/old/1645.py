#!/usr/bin/env python3
import sys
MOD = 998244353
def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0 for _ in range(20010)] for _ in range(N + 1)]
    offset = 10000
    dp[0][offset] = 1
    for i in range(N):
        for j in range(20010):
            if not dp[i][j]:
                continue
            dp[i + 1][j + A[i]] += dp[i][j]
            dp[i + 1][j - A[i]] += dp[i][j]
    ans = 0
    for j in range(20010):
        ans += abs(j - offset) * dp[-1][j]
        ans %= MOD
    print(ans % MOD)
    return

if __name__ == '__main__':
    main()