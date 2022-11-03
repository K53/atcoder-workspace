#!/usr/bin/env python3
import sys

def main():
    H, W = map(int, input().split())
    G = []
    dp = [[[0] * 2 for _ in range(W) ] for _ in range(H)]
    for _ in range(H):
        G.append(list(map(int, input().split())))
    dp[0][0][0] = G[0][0]

    for hh in range(H):
        for ww in range(W):
            for i in range(2):
                # 横
                if ww + 1 < W:
                    # 勝利
                    if G[hh][ww + 1] < dp[hh][ww][i]:
                        dp[hh][ww + 1][i] = max(dp[hh][ww + 1][i], dp[hh][ww][i] + G[hh][ww + 1])
                    else:
                        # continue
                        if i == 0 and not (hh == H - 1 and ww + 1 == W - 1):
                            dp[hh][ww + 1][1] = max(dp[hh][ww + 1][1], dp[hh][ww][0])
                        # 敗北
                        else:
                            pass 
                # 縦
                if hh + 1 < H:
                    # 勝利
                    if G[hh + 1][ww] < dp[hh][ww][i]:
                        dp[hh + 1][ww][i] = max(dp[hh + 1][ww][i], dp[hh][ww][i] + G[hh + 1][ww])
                    else:
                        # continue
                        if i == 0 and not (hh + 1 == H - 1 and ww == W - 1):
                            dp[hh + 1][ww][1] = max(dp[hh + 1][ww][1], dp[hh][ww][0])
                        # 敗北
                        else:
                            pass 
    if dp[-1][-1][0] > 0 or  dp[-1][-1][1] > 0:
        print("Yes")
    else:
        print("No")
    return


if __name__ == '__main__':
    main()