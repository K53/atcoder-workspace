#!/usr/bin/env python3


def main():
    INF = 10 ** 16
    N, M = map(int, input().split())
    A = []
    C = []
    for _ in range(M):
        a, b = map(int, input().split())
        c = list(map(int, input().split()))
        A.append(a)
        tmp = 0
        for i in c:
            tmp += 2 ** (i - 1)
        C.append(tmp)
    pattern = 2 ** N
    dp = [[INF] * pattern for _ in range(M + 1)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(pattern):
            if dp[i][j] == INF:
                continue
            # 使わない
            dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
            # 使う
            dp[i + 1][j | C[i]] = min(dp[i][j] + A[i], dp[i + 1][j | C[i]])

    print(-1 if dp[-1][-1] == INF else dp[-1][-1])

if __name__ == '__main__':
    main()
