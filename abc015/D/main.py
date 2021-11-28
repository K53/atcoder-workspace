#!/usr/bin/env python3
from sys import stdin

def main():
    W = int(stdin.readline())
    N, K = map(int, stdin.readline().split())
    AB = [tuple(map(int, stdin.readline().split())) for _ in range(N)]
    dp = [[0] * (W + 1) for _ in range(K + 1)] # dp[i][w] := i枚w以下の最大値
    c = 100
    for aa, bb in AB:
        for kk in range(K + 1):
            # if kk + 1 > K:
            #     continue
            for ww in range(W + 1):
                if ww + aa <= W and kk + 1 <= K:
                    dp[kk + 1][ww + aa] = max(dp[kk + 1][ww + aa], dp[kk][ww] + bb)
                if c > 0:
                    print(aa, bb, kk, ww)
                    for i in range(len(dp)):
                        print(dp[i])
                    c -= 1
                    print("-------")
    print(dp[K][W])
    # for i in range(len(dp)):
    #     print(dp[i])
    return


# def main():
#     W = int(stdin.readline())
#     N, K = map(int, stdin.readline().split())
#     AB =[tuple(map(int, stdin.readline().split())) for _ in range(N)]
#     dp = [[[-1] * (W + 1) for _ in range(K + 1)] for _ in range(N + 1)]
#     dp[0][0][0] = 0
#     for nn in range(N):
#         aa = AB[nn][0]
#         bb = AB[nn][1]
#         for ww in range(W + 1):
#             for kk in range(K + 1):
#                 if dp[nn][kk][ww] == -1:
#                     continue
#                 if ww + aa <= W and kk + 1 <= K:
#                     dp[nn + 1][kk + 1][ww + aa] = max(dp[nn + 1][kk + 1][ww + aa], dp[nn][kk][ww] + bb)
#                 dp[nn + 1][kk][ww] = max(dp[nn + 1][kk][ww], dp[nn][kk][ww])
#     ans = -1
#     for ww in range(W + 1):
#         for kk in range(K + 1):
#             ans = max(ans, dp[N][kk][ww])
#     print(ans)
#     return

if __name__ == '__main__':
    main()

