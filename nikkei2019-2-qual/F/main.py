#!/usr/bin/env python3
import sys

MOD = 998244353  # type: int


def solve(N: int, A: "List[str]"):
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(N - 1)]  # type: "List[str]"
    solve(N, A)

if __name__ == '__main__':
    main()
