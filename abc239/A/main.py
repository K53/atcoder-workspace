#!/usr/bin/env python3
import math
import sys


def solve(H: int):
    print(math.sqrt(H * (12800000 + H)))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    solve(H)

if __name__ == '__main__':
    main()
