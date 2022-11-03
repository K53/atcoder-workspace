#!/usr/bin/env python3
INF = 10 ** 16
def main():
    N, M = map(int, input().split())
    if N == 1:
        print(0)
        return
    G = []
    for _ in range(N):
        G.append(list(map(int, input().split())))
    ans = 0
    if M == 1:
        for i in range(N):
            ans += G[i][0]
        print(ans)
        return
    dp = [G[0]] + [[INF] * M for _ in range(N - 1)]
    tmp = sorted(G[0])
    mins = [tmp[0], tmp[1]]
    mins_next = []
    for i in range(1, N):
        for j in range(M):
            up = mins[0] if dp[i - 1][j] != mins[0] else mins[1]
            c = min(dp[i - 1][j] + G[i][j], up + G[i - 1][j] + G[i][j])
            dp[i][j] = c
            mins_next.append(c)
            mins_next.sort()
            mins_next = mins_next[:2]
        mins = mins_next
        mins_next = []
    # for i in range(N):
    #     print(dp[i])
    print(min(dp[-1]))
    return

if __name__ == '__main__':
    main()