#!/usr/bin/env python3
import sys
from collections import defaultdict

def solve(N: int, A: "List[int]"):
    ans = N * (N - 1) // 2
    d = defaultdict(int)
    for aa in A:
        d[aa] += 1
    for i, val in d.items():
        ans -= val * (val - 1) // 2
    print(ans)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
