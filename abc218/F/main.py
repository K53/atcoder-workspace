#!/usr/bin/env python3
import sys


def solve(N: int, M: int, s: "List[int]", t: "List[int]"):
    return


# Generated by 2.8.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    s = [int()] * (M)  # type: "List[int]"
    t = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, M, s, t)

if __name__ == '__main__':
    main()
