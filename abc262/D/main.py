#!/usr/bin/env python3
from collections import defaultdict
import sys

MOD = 998244353  # type: int


def solve(N: int, a: "List[int]"):
    dp = [[[0 for _ in range(N + 1) ] for _ in range(N + 1)] for _ in range(N + 1)]
    # for i in range(N + 1):
    #     for j in range(N + 1):
    #         print(dp[i][j])

    dp[0][0][0] = 1
    for i in range(N + 1): # シート
        for j in range(1, N + 1): # 回目
            asindex = j - 1
            for k in range(N + 1):
                if dp[i][j - 1][k] == 0:
                    continue
                # とらない
                dp[i][j][k] += dp[i][j - 1][k]
                # とる
                dp[i + 1][j][k + (a[asindex] % (i + 1))] += dp[i][j - 1][k]

    ans = 0
    # for i in range(N + 1):
    #     for j in range(N + 1):
    #         print(dp[i][j])
        # print("---")
    for i in range(1, N + 1):
        ans += dp[i][N][0]
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
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
