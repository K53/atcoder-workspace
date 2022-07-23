#!/usr/bin/env python3
import sys
INF = 10 ** 6

def solve(N: int, M: int, X: "List[int]", C: "List[int]", Y: "List[int]"):
    dp = [[-INF for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0] = 0
    d = dict()
    for cc, yy in zip(C,Y):
        d[cc] = yy
    pre = 0
    mx = 0
    for i in range(N):
        for mm in range(N):
            if dp[i][mm] == -INF:
                continue
            if mm + 1 in d:
                dp[i + 1][mm + 1] = max(dp[i + 1][mm + 1], dp[i][mm] + X[i] + d[mm + 1])
            else:
                dp[i + 1][mm + 1] = max(dp[i + 1][mm + 1], dp[i][mm] + X[i])
            mx = max(mx, dp[i + 1][mm + 1])
        dp[i + 1][0] = pre
        pre = mx
        mx = 0
    # for i in range(N + 1):
        # print(dp[i])
    print(pre)
            

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        C[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, X, C, Y)

if __name__ == '__main__':
    main()
