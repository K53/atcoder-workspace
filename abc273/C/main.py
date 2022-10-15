#!/usr/bin/env python3
from bisect import bisect_right
from collections import Counter
import sys


def solve(N: int, A: "List[int]"):
    ans = []
    L = sorted(list(set(A)))
    for i in range(N):
        # print(len(L) - bisect_right(L, A[i]))
        ans.append(len(L) - bisect_right(L, A[i]))
    c = Counter(ans)
    # print(c)
    for i in range(N):
        print(c[i])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
