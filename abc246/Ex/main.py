#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, Q: int, S: str, x: "List[int]", c: "List[str]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    x = [int()] * (Q)  # type: "List[int]"
    c = [str()] * (Q)  # type: "List[str]"
    for i in range(Q):
        x[i] = int(next(tokens))
        c[i] = next(tokens)
    solve(N, Q, S, x, c)

if __name__ == '__main__':
    main()
