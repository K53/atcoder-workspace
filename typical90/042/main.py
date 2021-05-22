#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(K: int):
    if K % 9 != 0:
        print(0)
        return
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in range(K + 1):
        B = min(i, 9)
        for j in range(1, B + 1):
            dp[i] = (dp[i] + dp[i - j]) % MOD
    print(dp[K])
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    solve(K)

if __name__ == '__main__':
    main()