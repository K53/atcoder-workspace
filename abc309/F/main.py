#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, h: "List[int]", w: "List[int]", d: "List[int]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int()] * (N)  # type: "List[int]"
    w = [int()] * (N)  # type: "List[int]"
    d = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        h[i] = int(next(tokens))
        w[i] = int(next(tokens))
        d[i] = int(next(tokens))
    solve(N, h, w, d)

if __name__ == '__main__':
    main()
