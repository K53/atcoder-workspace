#!/usr/bin/env python3
import sys


def solve(A: str, B: str):
    print(A if len(A) > len(B) else B)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = next(tokens)  # type: str
    B = next(tokens)  # type: str
    solve(A, B)

if __name__ == '__main__':
    main()
