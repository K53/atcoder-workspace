#!/usr/bin/env python3
import sys


def solve(W: int, H: int, x: int, y: int):
    k = 0
    if H / 2 == y and W / 2 == x:
        k = 1
    print(W * H / 2, k)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    W = int(next(tokens))  # type: int
    H = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(W, H, x, y)

if __name__ == '__main__':
    main()
