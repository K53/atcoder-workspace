#!/usr/bin/env python3
import sys


def solve(N: int, x: "List[int]", y: "List[int]", Q: int, a: "List[int]", b: "List[int]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N - 1)  # type: "List[int]"
    y = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    Q = int(next(tokens))  # type: int
    a = [int()] * (Q)  # type: "List[int]"
    b = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        a[i] = int(next(tokens))
        b[i] = int(next(tokens))
    solve(N, x, y, Q, a, b)

if __name__ == '__main__':
    main()
