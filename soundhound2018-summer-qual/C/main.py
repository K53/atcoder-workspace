#!/usr/bin/env python3
import sys


def solve(n: int, m: int, d: int):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    n = int(next(tokens))  # type: int
    m = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(n, m, d)

if __name__ == '__main__':
    main()