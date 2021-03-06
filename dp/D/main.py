#!/usr/bin/env python3
import sys

def solve(N: int, W: int, w: "List[int]", v: "List[int]"):
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(W + 1):
            # i番目の品を選ばない
            dp[i][j] = max(dp[i - 1][j], dp[i][j])
            # i - 1番目の品を選ぶ
            if j + w[i - 1] < W + 1:
                dp[i][j + w[i - 1]] = dp[i - 1][j] + v[i - 1]
    print(dp[-1][-1])
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    v = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, W, w, v)

if __name__ == '__main__':
    main()
