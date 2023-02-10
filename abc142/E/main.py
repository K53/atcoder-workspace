#!/usr/bin/env python3
INF = 10 ** 16

def main():
    INF = 10 ** 16
    N, M = map(int, input().split())
    A = []
    keys = []
    for i in range(M):
        aa, _ = map(int, input().split())
        A.append(aa)
        bitk = 0
        for c in list(map(int, input().split())):
            bitk += 2 ** (c - 1)
        keys.append(bitk)
    
    dp = [[INF] * (2 ** N) for _ in range(M + 1)]
    dp[0][0] = 0
    for i in range(M):
        for k in range(2 ** N):
            if dp[i][k] == INF:
                continue
            dp[i + 1][k | keys[i]] = min(dp[i + 1][k | keys[i]], dp[i][k] + A[i])
            dp[i + 1][k] = min(dp[i + 1][k], dp[i][k])
    print(-1 if dp[-1][-1] == INF else dp[-1][-1])
    


if __name__ == '__main__':
    main()
