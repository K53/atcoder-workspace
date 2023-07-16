#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", S: str):
    ans = 0
    for mm in range(3):
        for ee in range(3):
            for xx in range(3):
                mex = -1
                s = set((mm, ee, xx))
                for i in range(4):
                    if i not in s:
                        mex = i
                        break
                if mex == 0:
                    continue
                dp = [[1] + [0 for _ in range(3)] for _ in range(N + 1)]
                pt = [("M", mm), ("E", ee), ("X", xx)]
                for i in range(N):
                    for j in range(3):
                        if (S[i], A[i]) == pt[j]:
                            dp[i + 1][j + 1] += dp[i][j]
                        dp[i + 1][j + 1] += dp[i][j + 1]
                ans += dp[-1][-1] * mex
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    S = next(tokens)  # type: str
    solve(N, A, S)

if __name__ == '__main__':
    main()