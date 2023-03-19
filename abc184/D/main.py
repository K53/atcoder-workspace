#!/usr/bin/env python3
import sys
INF = 10 ** 16

def solve(A: int, B: int, C: int):
    dp = [[[INF] * 101 for _ in range(101)] for _ in range(101)]
    for i in range(101):
        for j in range(101):
            dp[i][j][100] = 0 
            dp[i][100][j] = 0 
            dp[100][i][j] = 0 
    for i in reversed(range(100)):
        for j in reversed(range(100)):
            for k in reversed(range(100)):
                if i == j == k == 0:
                    continue
                dp[i][j][k] = ((dp[i + 1][j][k] + 1) * i + \
                                (dp[i][j + 1][k] + 1) * j + \
                                (dp[i][j][k + 1] + 1) * k) / (i + j + k)
    print(dp[A][B][C])
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)

if __name__ == '__main__':
    main()
