#!/usr/bin/env python3
import sys
from collections import Counter

def solve(N: int, A: "List[int]"):
    d = Counter(A)
    keys = list(d.keys())
    L = len(keys)
    ans = 0
    for i in range(L - 1):
        for j in range(i + 1, L):
            ans += (keys[i] - keys[j]) ** 2 * (d[keys[i]] * d[keys[j]])
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
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
