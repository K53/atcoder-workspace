#!/usr/bin/env python3
import sys
from itertools import groupby

def solve(N: int, h: "List[int]"):
    ans = 0
    for border in range(max(h)):
        l = [hh > border for hh in h]
        grouped = groupby(l)
        ll = [k for k, _ in grouped]
        # print(ll)
        ans += ll.count(True)
    print(ans)
    return

# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    h = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, h)

if __name__ == '__main__':
    main()
