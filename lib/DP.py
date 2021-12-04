# DP高速化 (累積和)

def solve():
    from itertools import accumulate
    N = 10
    K = 10
    a = []
    MOD = 10 * 9 + 7
    # ----
    dp = [[0] * (K + 1) for _ in range(N + 1)] # DPテーブルの作成
    sdp = [0] * (K + 1)                        # 累積和テーブルの作成(累積和は最後の列のみ持てばいい(DP遷移が最後の累積和に依存する場合))
    dp[0][0] = 1                               # DPテーブルの初期化
    sdp = list(accumulate(dp[0]))              # 累積和テーブルの初期化

    # print(sdp)
    for i in range(1, N + 1):
        for num in range(K + 1):               # 列のDPテーブル更新
            dp[i][num] = sdp[num]
            dp[i][num] %= MOD
        sdp = list(accumulate(dp[i]))          # 列のテーブル更新を終えたら累積和を算出。
        # print(i, sdp)
    print(dp[N][K] % MOD)