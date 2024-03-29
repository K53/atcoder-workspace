#!/usr/bin/env python3
import sys
from collections import defaultdict


def solve(Q: int, t: "List[int]", x: "List[int]"):
    N = 2 ** 20
    ok = [i for i in range(N)]
    d = defaultdict(lambda: -1)
    m = 2 ** 20
    for tt, xx in zip(t, x):
        if tt == 1:
            h = xx % m
            d[h] = xx
        else:
            h = xx % m
            print(d[h])
            
        

    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    Q = int(next(tokens))  # type: int
    t = [int()] * (Q)  # type: "List[int]"
    x = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
    solve(Q, t, x)

if __name__ == '__main__':
    main()
