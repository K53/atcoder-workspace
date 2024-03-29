#!/usr/bin/env python3
import sys


def solve(N: int):
    dp = [1 / 6] * 6
    ans = 3.5
    for k in range(N):
        num = 0
        next = 0
        for i in range(N):
            if i >= ans * 5 / 6:
                next = i * dp[i]
                continue
            num += 1
            
        num / 6

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    solve(N)

if __name__ == '__main__':
    main()
