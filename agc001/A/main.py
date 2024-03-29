#!/usr/bin/env python3
import sys


def solve(N: int, L: "List[int]"):
    L.sort()
    ans = 0
    for i in range(0, 2 * N, 2):
        ans += min(L[i], L[i + 1])
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
    L = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, L)

if __name__ == '__main__':
    main()
