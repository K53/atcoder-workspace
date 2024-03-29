#!/usr/bin/env python3
import sys


def solve(N: int):
    ans = 0
    for a in range(1, int(pow(N, 0.34) + 1)):
        for b in range(a, int(pow(N, 0.5) + 1)):
            if a * b > N:
                break
            c, q = divmod(N, a * b)
            if c >= b:
                # print(a, b, c)
                ans += c - b + 1
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
