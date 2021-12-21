#!/usr/bin/env python3
import sys


def solve(N: int):
    ans = 0
    for a in range(1, 4650):
        for b in range(a, N // a + 1):
            # print(a,b, N // (a * b))
            k = N // (a * b) - b + 1
            ans += max(0, k)
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
    solve(N)

if __name__ == '__main__':
    main()