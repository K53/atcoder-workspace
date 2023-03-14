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
        c = list(map(int, input().split()))
        k = 0
        for cc in c:
            k += 1 << (cc - 1)
        keys.append(k)
            
    dp = [[INF] * (2 ** N) for _ in range(M + 1)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(2 ** N):
            if dp[i][j] == INF:
                continue
            dp[i + 1][j | keys[i]] = min(dp[i + 1][j | keys[i]], dp[i][j] + A[i])
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    ans = dp[-1][-1]
    print(-1 if ans == INF else ans)
    return

if __name__ == '__main__':
    main()
