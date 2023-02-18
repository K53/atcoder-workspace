#!/usr/bin/env python3
import sys
INF = 10 ** 18

def solve(N: int, K: int, A: "List[int]"):
    # dp[i][smaller] := i桁目まで確定していて、上限 K と比較した時に 
    # smaller = 0 : Kにちょうど一致する。 (0か1に遷移する。)
    # smaller = 1 : Kより小さくなっている。 (1にしか遷移しない。)
    #   ときの最大値.
    dp = [[-INF] * 2 for _ in range(51)]
    dp[0][0] = 0
    for dig in range(50):
        mask = 1 << 50 - dig - 1 # 上の桁から決めていく必要があるので最上位の桁までシフト

        num = 0 # Aのうちdig桁目が立っているビットの個数
        for aa in A:
            if aa & mask:
                num += 1
        
        # Xにおいて、dig桁目を1にしてビットを立てる時にf(x)に加算される数と、0にした時に加算される数をそれぞれ出す。
        val0 = mask * num
        val1 = mask * (N - num)
        
        if dp[dig][1] != -INF:
            # smaller=1なので、dig+1桁目のbitを立てる場合と立てないようが立てまいがsmaller=1のまま遷移する。
            # この時、立てる片手ないかは自由なので大きくなる方を選ぶ。=+max(val0, val1)
            dp[dig + 1][1] = max(dp[dig + 1][1], dp[dig][1] + max(val0, val1))
        if dp[dig][0] != -INF:
            # smaller=0から1への遷移。dig桁目までは上限 K と完全一致している = smallerに移るにはdig+1桁目を譲るしかない。
            if K & mask: 
                # 上限Kの方でmaskビット目のビットが立っているなら値を0にして譲れる。そうでないならsmaller=0にしか遷移できない。
                dp[dig + 1][1] = max(dp[dig + 1][1], dp[dig][0] + val0)
                # smaller=0から0への遷移。ビットが立ってるのに合わせる。
                dp[dig + 1][0] = max(dp[dig + 1][0], dp[dig][0] + val1)
            else:
                # ビットが立ってないなら0->1の繊維は起きない。
                # 0->0の遷移のみ。
                dp[dig + 1][0] = max(dp[dig + 1][0], dp[dig][0] + val0)
    print(max(dp[-1][0], dp[-1][1]))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A)

if __name__ == '__main__':
    main()
