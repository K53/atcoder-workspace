#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, X: int, A: "List[int]", B: "List[int]"):
    yyy = X + 1
    dp = [[0 for _ in range(yyy)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(N):
        yen, num = A[i], B[i]
        for y in range(yyy):
            if dp[i][y]:
                # print(i, y)
                dp[i + 1][y] = 1
                for mai in range(num):
                    if y + yen * (mai + 1) < yyy:
                        dp[i + 1][y + yen * (mai + 1)] = 1
                    
    # for i in range(N + 1):
    #     print(dp[i])
    # for i in range(yyy):
    #     if dp[-1][i] == 1:
    #         print(i)
    print(YES if dp[-1][-1] else NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, X, A, B)

if __name__ == '__main__':
    main()
