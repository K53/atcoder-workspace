#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]", Q: int, x: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    Q = int(next(tokens))  # type: int
    x = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, S, Q, x)

if __name__ == '__main__':
    main()
