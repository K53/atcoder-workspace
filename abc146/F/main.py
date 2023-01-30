#!/usr/bin/env python3
import sys
from itertools import accumulate

def solve():
    N = 10
    K = 10
    a = []
    MOD = 10 * 9 + 7
    # ----
    dp = [0 for _ in range(N + 2)] # DPテーブルの作成
    sdp = [0] * (N + 2)                        # 累積和テーブルの作成(累積和は最後の列のみ持てばいい(DP遷移が最後の累積和に依存する場合))
    dp[0] = 1                               # DPテーブルの初期化
    sdp = list(accumulate(dp[0]))              # 累積和テーブルの初期化

    # print(sdp)
    for i in range(1, N + 1):
        for num in range(K + 1):               # 列のDPテーブル更新
            dp[i][num] = sdp[num]
            dp[i][num] %= MOD
        sdp = list(accumulate(dp[i]))          # 列のテーブル更新を終えたら累積和を算出。
        # print(i, sdp)
    print(dp[N][K] % MOD)
def solve(N: int, M: int, S: str):
    dp = []
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, M, S)

if __name__ == '__main__':
    main()
