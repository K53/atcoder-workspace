#!/usr/bin/env python3
import sys


def solve(N: int):
    ans = []
    for i in range(N + 1):
        for j in range(1, 10):
            p, q = divmod(N, j)
            pi, qi = divmod(i, p)
            if q == 0 and qi == 0:
                ans.append(j)
                break
        else:
            ans.append("-")
    print(*ans, sep="")
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