#!/usr/bin/env python3
import sys


def solve(N: int, K: int, s: "List[int]"):
    l = 0
    r = 0
    ans = 0
    mul = 1
    for _ in range(N):
        while r < N and mul <= K:
            print("#", l, r, s[r], mul)
            mul *= s[r]
            print(mul, r)
            r += 1
            print(r)
        if r < N and mul > K:
            ans = max(ans, r - l + 1)
            print(">", l, r, mul)
            mul //= s[l]
            l += 1
    ans = max(ans, l - r + 1)
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
    K = int(next(tokens))  # type: int
    s = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, s)

if __name__ == '__main__':
    main()
