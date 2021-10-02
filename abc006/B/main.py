#!/usr/bin/env python3
import sys

MOD = 10007  # type: int


def solve(n: int):
    dp = [0] * (10 ** 6)
    dp[2] = 1
    for i in range(3, 10 ** 6):
        dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD
    print(dp[n - 1])
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    solve(n)

if __name__ == '__main__':
    main()