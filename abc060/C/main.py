#!/usr/bin/env python3
import sys


def solve(N: int, T: int, t: "List[int]"):
    start = 0
    ans = 0
    for i in range(N - 1):
        d = t[i + 1] - t[i]
        if T >= d:
            continue
        ans += t[i] - start + T
        start = t[i + 1]
    ans += t[-1] - start + T
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
    T = int(next(tokens))  # type: int
    t = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, T, t)

if __name__ == '__main__':
    main()
