#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, S: int, a: "List[int]", b: "List[int]"):
    maxS = 10000
    # print(list(range(14 + 1)))
    dp = [[0 for _ in range(maxS + 1)] for _ in range(N + 1)]
    dp[0][0] = 1
    for i in range(1, N + 1):
        for ss in range(maxS + 1):
            if dp[i - 1][ss] == 0:
                continue
            # front
            dp[i][ss + a[i - 1]] = 1
            # back
            dp[i][ss + b[i - 1]] = 1
    # for i in range(N + 1):
    #     print(dp[i])
    if not dp[N][S]:
        print(NO)
        return
    print(YES)
    rest = S
    ans = []
    for i in reversed(range(1, N + 1)):
        # print(i, a[i - 1], b[i - 1])
        if dp[i - 1][rest - a[i - 1]]:
            ans.append("H")
            rest -= a[i - 1]
        else:
            ans.append("T")
            rest -= b[i - 1]
    print(*ans[::-1], sep="")
        


    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    a = [int()] * (N)  # type: "List[int]"
    b = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, S, a, b)

if __name__ == '__main__':
    main()
