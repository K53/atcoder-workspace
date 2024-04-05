#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    dp = [[0] * 2 for _ in range(N + 1)]
    # dp[i][k] f(n, i)=kとなる個数 0<n<i
    for i in range(N):
        if S[i] == "1":
            dp[i + 1][1] = dp[i][0] + 1
            dp[i + 1][0] = dp[i][1]
        else:
            dp[i + 1][1] = dp[i][0] + dp[i][1]
            dp[i + 1][0] = 1
    ans = 0
    for i in range(N + 1):
        ans += dp[i][1]
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
