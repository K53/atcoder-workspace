#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    INF = 10 ** 9
    dp = [INF] * N
    dp[0] = 0
    for i in range(N - 1):
        dp[i + 1] = min(dp[i + 1], dp[i] + abs(a[i] - a[i + 1]))
        if i + 2 < N:
            dp[i + 2] = min(dp[i + 2], dp[i] + abs(a[i] - a[i + 2]))
    print(dp[-1])
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()