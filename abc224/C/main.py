#!/usr/bin/env python3
import sys


def solve(N: int, X: "List[int]", Y: "List[int]"):
    from itertools import combinations
    nn = combinations(range(N), 3)
    ans = N * (N - 1) * (N - 2) // 6
    c = 0
    for i in nn:
        x1, y1 = X[i[0]], Y[i[0]]
        x2, y2 = X[i[1]], Y[i[1]]
        x3, y3 = X[i[2]], Y[i[2]]
        if (x1 - x2) * (y2 - y3) == (x2 - x3) * (y1 - y2):
            c += 1
    ans -= c
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
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, X, Y)

if __name__ == '__main__':
    main()
