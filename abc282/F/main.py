#!/usr/bin/env python3
import sys


def solve(l_i: str, r_i: str):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    l_i = next(tokens)  # type: str
    r_i = next(tokens)  # type: str
    solve(l_i, r_i)

if __name__ == '__main__':
    main()
