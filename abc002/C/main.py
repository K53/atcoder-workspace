#!/usr/bin/env python3
import sys


def solve(x_a: int, y_a: int, x_b: int, y_b: int, x_c: int, y_c: int):
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x_a = int(next(tokens))  # type: int
    y_a = int(next(tokens))  # type: int
    x_b = int(next(tokens))  # type: int
    y_b = int(next(tokens))  # type: int
    x_c = int(next(tokens))  # type: int
    y_c = int(next(tokens))  # type: int
    solve(x_a, y_a, x_b, y_b, x_c, y_c)

if __name__ == '__main__':
    main()
