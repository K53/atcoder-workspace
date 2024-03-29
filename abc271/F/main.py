#!/usr/bin/env python3
import sys
from collections import defaultdict


def solve(N: int, a: "List[List[int]]"):
    d = defaultdict(lambda : defaultdict(int))
    def hop(x: int, y: int, val: int):
        if x + y >= N - 1:
            # print(val, "in")
            d[(y, x)][val] += 1
            return
        # print(x, y)
        # print(val, "->", val ^ a[y][x])
        val ^= a[y][x]
        hop(x + 1, y, val)
        hop(x, y + 1, val)
    
    dd = defaultdict(lambda : defaultdict(int))
    def hop2(x: int, y: int, val: int):
        if (N - 1) - x + (N - 1) - y >= N - 1:
            dd[((N - 1) - x, (N - 1) - y)][val] += 1
            return
        # print(x, y)
        val ^= a[y][x]
        hop2(x - 1, y, val)
        hop2(x, y - 1, val)

    hop(0, 0, 0)
    hop2(N - 1, N - 1, 0)

    ans = 0
    for key, vals in d.items():
        for num, count in vals.items():
            s = num ^ a[key[0]][key[1]]
            ans += dd[key][s] * count
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
    a = [[int(next(tokens)) for _ in range(N)] for _ in range(N)]  # type: "List[List[int]]"
    solve(N, a)

if __name__ == '__main__':
    main()
