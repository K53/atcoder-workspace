#!/usr/bin/env python3
import sys


def solve(R: int, C: int, K: int, r: "List[int]", c: "List[int]", v: "List[int]"):
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    r = [int()] * (K)  # type: "List[int]"
    c = [int()] * (K)  # type: "List[int]"
    v = [int()] * (K)  # type: "List[int]"
    for i in range(K):
        r[i] = int(next(tokens))
        c[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(R, C, K, r, c, v)

if __name__ == '__main__':
    main()
