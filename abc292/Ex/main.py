#!/usr/bin/env python3
import sys


def solve(N: int, B: int, Q: int, a: "List[int]", c: "List[int]", x: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    c = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        c[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(N, B, Q, a, c, x)

if __name__ == '__main__':
    main()