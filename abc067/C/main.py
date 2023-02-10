#!/usr/bin/env python3
import sys
from itertools import accumulate

def solve(N: int, a: "List[int]"):
    S = sum(a)
    l = list(accumulate(a))
    ans = 10 ** 16
    for i in range(N - 1):
        ans = min(ans, abs(l[i] - (S - l[i])))
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
