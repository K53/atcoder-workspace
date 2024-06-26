#!/usr/bin/env python3
import sys


def solve(A: int, M: int, L: int, R: int):
    ans = 0
    for k in range(1000):
        cur = A + k * M
        if cur > R:
            break
        else:
            ans += 1
    for k in range(-1000, 0):
        cur = A + k * M
        if cur < L:
            break
        else:
            ans += 1
    print(ans)
    return

# Generated by 2.13.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    R = int(next(tokens))  # type: int
    solve(A, M, L, R)

if __name__ == '__main__':
    main()
