#!/usr/bin/env python3
INF = 10 ** 16
def main():
    N, I = map(int, input().split())
    dp = [[-INF] * (I + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    ramen = []
    for _ in range(N):
        s, a = map(int, input().split())
        ramen.append((s, a))
    for i in range(N):
        for j in range(I + 1):
            s, a = ramen[i]
            if dp[i][j] == -INF:
                continue
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if j + s < I + 1:
                dp[i + 1][j + s] = max(dp[i + 1][j + s], dp[i][j] + a)
    print(max(dp[-1]))
if __name__ == '__main__':
    main()