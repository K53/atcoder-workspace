#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    dp1 = [[0] * (N - 1) for _ in range(2)]
    dp2 = [[0] * (N - 1) for _ in range(2)]

    dp1[0][0] = A[-1]
    dp1[1][0] = 10 ** 16

    dp2[0][0] = 10 ** 16
    dp2[1][0] = A[0]
    for i in range(0, N - 2):
        dp1[0][i + 1] = min(dp1[0][i] + A[i], dp1[1][i] + 0)
        dp1[1][i + 1] = min(dp1[0][i] + A[i + 1], dp1[1][i] + A[i + 1])

        dp2[0][i + 1] = min(dp2[0][i] + A[i], dp2[1][i] + 0)
        dp2[1][i + 1] = min(dp2[0][i] + A[i + 1], dp2[1][i] + A[i + 1])
    # print(dp1[0])
    # print(dp1[1])
    # print()
    # print(dp2[0])
    # print(dp2[1])
    print(min(dp1[0][-1], dp1[1][-1], dp2[1][-1]))

    
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
    solve(N, A)

if __name__ == '__main__':
    main()
