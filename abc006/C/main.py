#!/usr/bin/env python3
import sys


def solve(N: int, M: int):
    if not 2 * N <= M <= 4 * N:
        print(-1, -1, -1)
        return
    center = 3 * N
    diff = M - center
    if diff > 0:
        print(0, N - diff, diff)
    else:
        print(-diff, N + diff, 0)
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
    solve(N, M)

if __name__ == '__main__':
    main()
