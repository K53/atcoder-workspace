#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    INF = 10 ** 18
    # dp[i][last] := i番目とi+1番目まで選び、i+1番目の符号がlast(0:反転なし,1:反転あり)の時の最大値
    dp = [[0, 0] for _ in range(N)]
    dp[0] = [A[0], -INF]
    for i in range(1, N):
        # print(i, "[0]", dp[i - 1][0] + A[i], dp[i - 1][1] + A[i])
        dp[i][0] = max(dp[i - 1][0] + A[i], dp[i - 1][1] + A[i])
        # print(i, "[1]", dp[i - 1][0] - (A[i - 1] * 2) - A[i], dp[i - 1][1] + (A[i - 1] * 2) - A[i])
        dp[i][1] = max(dp[i - 1][0] - (A[i - 1] * 2) - A[i], dp[i - 1][1] + (A[i - 1] * 2) - A[i])
    print(max(dp[-1]))
    return

# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
