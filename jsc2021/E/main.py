#!/usr/bin/env python3
import sys

NO = "impossible"  # type: str


def solve(K: int, S: str):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(K, S)

if __name__ == '__main__':
    main()