#!/usr/bin/env python3
import sys


def solve(N: int, A_x: int, A_y: int, B_x: int, B_y: int, S: "List[str]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A_x = int(next(tokens))  # type: int
    A_y = int(next(tokens))  # type: int
    B_x = int(next(tokens))  # type: int
    B_y = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, A_x, A_y, B_x, B_y, S)

if __name__ == '__main__':
    main()