#!/usr/bin/env python3
import sys
from itertools import accumulate

def solve(N: int, K: int, a: "List[int]"):
    s = [0] + list(accumulate(a))
    ans = 0
    for i in range(N - K + 1):
        ans += s[i + K] - s[i]
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
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, a)

if __name__ == '__main__':
    main()
