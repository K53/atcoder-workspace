#!/usr/bin/env python3
import sys


def solve(N: int, X: int, Y: int):
    red = 1
    blue = 0
    for i in reversed(range(1, N + 1)):
        if i >= 2:
            blue += red * X
            #--
            red += blue
            blue = blue * Y
        else:
            print(blue)
            return
    print(0)
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
    Y = int(next(tokens))  # type: int
    solve(N, X, Y)

if __name__ == '__main__':
    main()
