#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(D: int, T: int, S: int):
    print(YES if T * S >= D else NO)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    D = int(next(tokens))  # type: int
    T = int(next(tokens))  # type: int
    S = int(next(tokens))  # type: int
    solve(D, T, S)

if __name__ == '__main__':
    main()
