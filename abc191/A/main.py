#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(V: int, T: int, S: int, D: int):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    V = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(V, T, S, D)

if __name__ == '__main__':
    main()
