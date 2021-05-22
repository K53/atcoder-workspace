#!/usr/bin/env python3
import sys


# dp[a][b] := Aの残数a、Bの残数bの時の得点差
def solve(A: int, B: int, a: "List[int]", b: "List[int]"):
    dp = [[None] * (B + 1) for _ in range(A + 1)]
    dp[0][0] = 0
    for rest in range(1, A + B + 1):
        for aa in range(A + 1):
            bb = rest - aa
            if bb < 0:
                break
            if bb > B:
                continue
            # print(aa, bb)
            if (A + B - rest) % 2 == 0:
                if aa == 0:
                    dp[aa][bb] = dp[aa][bb - 1] + b[B - 1 - (bb - 1)]
                elif bb == 0:
                    dp[aa][bb] = dp[aa - 1][bb] + a[A - 1 - (aa - 1)]
                else:
                    dp[aa][bb] = max(dp[aa - 1][bb] + a[A - 1 - (aa - 1)], dp[aa][bb - 1] + b[B - 1 - (bb - 1)])
            else:
                if aa == 0:
                    dp[aa][bb] = dp[aa][bb - 1] - b[B - 1 - (bb - 1)]
                elif bb == 0:
                    dp[aa][bb] = dp[aa - 1][bb] - a[A - 1 - (aa - 1)]
                else:
                    dp[aa][bb] = min(dp[aa - 1][bb] - a[A - 1 - (aa - 1)], dp[aa][bb - 1] - b[B - 1 - (bb - 1)])
    # print(dp)
    print((dp[A][B] + sum(a) + sum(b)) // 2)
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
    a = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    solve(A, B, a, b)

if __name__ == '__main__':
    main()
