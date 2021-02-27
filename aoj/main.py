#!/usr/bin/env python3

# dp[{i個目まで選択可能な時}][{重さwまで選択可能な時}] = {最大価値}
# 品物、重さ共に0-Indexedで用意するため大きさはdp[N+1][W+1]
# ただし、0-Indexedでやると品物の番号ととずれるので注意。
#   = i個目の品物の取る取らないを判別した結果はdp[i+1]の列に書き込むことになる。
#
def main():
    N, W = map(int, input().split())
    dp = []
    for _ in range(N + 1):
        dp.append([0] * (W + 1))
    for i in range(N):
        v, w = map(int, input().split())
        for j in range(W + 1):
            if j - w < 0:
                dp[i + 1][j] = dp[i][j]
            else:
                dp[i + 1][j] = max(dp[i][j], dp[i][j - w] + v)
    
    print(dp[N][W])

        
    

    return
if __name__ == '__main__':
    main()