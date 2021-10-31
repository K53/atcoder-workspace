#!/usr/bin/env python3


def main():
    INF = 10 ** 16
    N, M = map(int, input().split())
    cost = []
    keys = []
    for _ in range(M):
        a, b = map(int, input().split())
        cost.append(a)
        cc = 0
        for i in list(map(int, input().split())):
            cc += 2 ** (i - 1)
        keys.append(cc)
    # print(cost)
    # print(keys)
    dp = [[INF] * (2 ** N) for _ in range(M + 1)]
    dp[0][0] = 0
    for mm in range(M):
        for nn in range(2 ** N):
            if dp[mm][nn] == INF:
                continue
            dp[mm + 1][nn | keys[mm]] = min(dp[mm + 1][nn | keys[mm]], dp[mm][nn] + cost[mm])
            dp[mm + 1][nn] = min(dp[mm + 1][nn], dp[mm][nn])
    print(-1 if dp[-1][-1] == INF else dp[-1][-1])
    return

if __name__ == '__main__':
    main()
