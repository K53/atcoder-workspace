#!/usr/bin/env python3
import sys


def solve(A: int, B: int):
    def d(S: str):
        # dp[dig][smaller] := 先頭からdig桁決定した時の4or9がsum個あるものが何通りあるのか。smaller = Falseでは上限に達しているということ。
        dp = [[[0] * 2 for _ in range(2)] for _ in range(len(S) + 1)]
        dp[0][0][0] = 1

        # for dig in range(len(S)):
        #     # dig桁目はNの上限でなく、dig+1桁目はなんでも良い時。
        #     dp[dig + 1][1][sum + 1] = dp[dig][1][sum] * 2
        #     dp[dig + 1][1][sum] = dp[dig][1][sum] * 8
        #     targetDigNum = int(S[dig])
        #     # dig桁目はNの上限であり、dig+1桁目はNの上限より小さい時。
        #     if 4 < targetDigNum < 9:
        #         dp[dig + 1][1][sum + 1] = dp[dig][1][sum]
        #         dp[dig + 1][1][sum] = dp[dig][1][sum] * (targetDigNum - 1)
        #     elif targetDigNum == 4:
        #         dp[dig + 1][1][sum + 1] = dp[dig][1][sum]
        #     # dig桁目はNの上限であり、dig+1桁目もNの上限である時。
        #     if targetDigNum == 4:
        #         dp[dig + 1][0][sum + 1] += dp[dig][0][sum]
        #     elif targetDigNum == 9:
        #         dp[dig + 1][0][sum + 1] += dp[dig][0][sum] * 2
        #     else:
        #         dp[dig + 1][0][sum] += dp[dig][0][sum]
        for dig in range(len(S)):
            targetDigNum = int(S[dig])
            for smaller in range(2):
                for fourOrNine in range(2):
                    ceil = 9 if smaller else targetDigNum
                    for num in range(ceil + 1):
                        next_smaller = 0
                        next_fourOrNine = 0
                        # 現状上限でない or 次の数字が上限じゃない なら次の桁も当然上限ではない。
                        if smaller == 1 or num < targetDigNum:
                            next_smaller = 1
                        if fourOrNine == 1 or num == 4 or num == 9:
                            next_fourOrNine = 1
                        dp[dig + 1][next_smaller][next_fourOrNine] += dp[dig][smaller][fourOrNine]
            

        return dp[-1][0][1] + dp[-1][1][1]
        # ans = 0
        # for i in range(2):
        #     for smaller in range(2):
        #         ans += dp[len(S)][smaller][i] * i
        # return ans
    print(d(str(B)) - d(str(A - 1)))
    # print(d(str(B)) - d(str(A - 1)))

    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()