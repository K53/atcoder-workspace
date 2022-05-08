#!/usr/bin/env python3
import sys
MOD = 998244353
def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[0 for _ in range(2)] for _ in range(N + 1)]
    for i in range(N):
        dp[i + 1][0] = max(dp[i])
        dp[i + 1][1] = dp[i][0] + A[i]
    now = max(dp[-1])
    print(now)
    ans = []
    for i in range(N + 1)[::-1]:
        if now == 0:
            break
        if dp[i][1] == now:
            ans.append(i)
            now -= A[i - 1]
    print(*ans[::-1], sep= " ")
    return

if __name__ == '__main__':
    main()