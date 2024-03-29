#!/usr/bin/env python3
import sys


def solve(R: int, G: int, B: int, N: int):
    ans = 0
    for rr in range(N + 1):
        for gg in range(N + 1):
            rest = N - (rr * R + gg * G)
            if rest < 0:
                break
            if rest % B == 0:
                # print(rr, gg)
                ans += 1
    print(ans)
    return


# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    G = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    N = int(next(tokens))  # type: int
    solve(R, G, B, N)

if __name__ == '__main__':
    main()
