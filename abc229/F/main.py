#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[int]", B: "List[int]"):
    dp = [[[0] * N for _ in range(2)] for _ in range(2)]
    INF = 10 ** 17
    dp[0][0][0] = 0
    dp[1][0][0] = -INF
    dp[0][1][0] = -INF
    dp[1][1][0] = A[0]
    for i in range(N - 1):
        dp[0][0][i + 1] = max(dp[0][0][i + 1], max(dp[0][0][i], dp[1][0][i] + B[i]))
        dp[1][0][i + 1] = max(dp[1][0][i + 1], max(dp[0][0][i] + B[i] + A[i + 1], dp[1][0][i] + A[i + 1]))
        dp[0][1][i + 1] = max(dp[0][1][i + 1], max(dp[0][1][i], dp[1][1][i] + B[i]))
        dp[1][1][i + 1] = max(dp[1][1][i + 1], max(dp[0][1][i] + B[i] + A[i + 1], dp[1][1][i] + A[i + 1]))
    
    dp[0][1][-1] += B[-1]
    dp[1][0][-1] += B[-1]
    # print(dp[0])
    # print(dp[1])
    ans = 0
    for i in range(2):
        for j in range(2):
            ans = max(ans, dp[i][j][-1])
    print(sum(A) + sum(B) - ans)
    return 


 
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
