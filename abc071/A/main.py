#!/usr/bin/env python3
import sys


def solve(x: int, a: int, b: int):
    if abs(x-a) > abs(x-b):
        print("B")
    else:
        print("A")
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    x = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    solve(x, a, b)

if __name__ == '__main__':
    main()
