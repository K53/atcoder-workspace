#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(D: int, N: str):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    N = next(tokens)  # type: str
    solve(D, N)

if __name__ == '__main__':
    main()