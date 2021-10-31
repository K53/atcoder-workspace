#!/usr/bin/env python3
import sys


def solve(N: int, M: int, A: "List[int]"):
    from itertools import accumulate
    from collections import defaultdict
    acc = [i % M for i in accumulate(A)]
    d = defaultdict(int)
    for i in acc:
        d[i] += 1
    ans = 0
    for num, c in d.items():
        if num == 0:
            ans += c
        ans += c * (c - 1) // 2
    print(ans)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
