#!/usr/bin/env python3
import sys


def solve(N: int, K: int, w: "List[int]", p: "List[int]"):
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    w = [int()] * (N)  # type: "List[int]"
    p = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        w[i] = int(next(tokens))
        p[i] = int(next(tokens))
    solve(N, K, w, p)

if __name__ == '__main__':
    main()
