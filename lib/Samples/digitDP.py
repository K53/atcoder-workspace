
# 0〜Nまでの数全ての個数を求める桁DP。 = N + 1

def solve(N: str):
    # 文字列として扱うので最大の長さを取得。これがDP配列長になる。
    maxDig = len(str(N)) + 1
    S = str(N)
    # dp[i][isless][K] := i桁目まで決めた時、かつその数が上限[以下|ちょうど]である場合0でない数の個数
    dp = [[0] * 2 for _ in range(maxDig)]
    dp[0][0] = 1
    for dig in range(maxDig - 1):
        for isless in range(2):
            # 上限を確認 その桁に0〜maxNumまでなら並べられる。
            maxNum =  ord(S[dig]) - ord("0")

            # 次の桁にnextを置くことを考える。
            for next in range(10):
                # islessフラグが立ってるなら0~9まで置けるので気にしなくていい。そうでないなら気にする。
                if next > maxNum and isless == 0:
                    continue

                # 遷移
                # isless=1 → isless=1 にしか行かない。
                # isless=0 → 次の桁も上限ギリギリなら isless=0 に行ける。
                #          → そうでないなら isless=1に落ちる。
                if isless == 0 and next == maxNum:
                    next_isless = 0
                else:
                    next_isless = 1
                    
                dp[dig + 1][next_isless] += dp[dig][isless]
    print(dp[-1][0] + dp[-1][1])
    return
