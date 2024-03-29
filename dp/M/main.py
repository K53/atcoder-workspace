#!/usr/bin/env python3
import sys
from itertools import accumulate

MOD = 1000000007  # type: int


def solve(N: int, K: int, a: "List[int]"):
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    sdp = [0] * (K + 1)
    dp[0][0] = 1
    sdp = list(accumulate(dp[0]))

    # print(sdp)
    for i in range(1, N + 1):
        for num in range(K + 1):
            dp[i][num] = sdp[num] - (sdp[num - a[i - 1] - 1] if num - a[i - 1] - 1 >= 0 else 0)
            dp[i][num] %= MOD
        sdp = list(accumulate(dp[i]))
        # print(i, sdp)
    print(dp[N][K] % MOD)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)

if __name__ == '__main__':
    main()
