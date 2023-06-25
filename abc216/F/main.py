#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, A: "List[int]", B: "List[int]"):
    AB = sorted([(aa, bb) for aa, bb in zip(A, B)])
    mA = max(A) + 1
    dp = [[0 for _ in range(mA)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        for num in range(mA):
            dp[i + 1][num] += dp[i][num]
            dp[i + 1][num] %= MOD
            if num + AB[i][1] < mA:
                dp[i + 1][num + AB[i][1]] += dp[i][num]
                dp[i + 1][num + AB[i][1]] %= MOD
    ans = 0
    for i in range(N):
        for num in range(mA):
            if num <= AB[i][0] - AB[i][1]:
                ans += dp[i][num]
                ans %= MOD
    print(ans)
    return


# Generated by 2.8.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    B = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A, B)

if __name__ == '__main__':
    main()
