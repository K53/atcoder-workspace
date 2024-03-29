#!/usr/bin/env python3
import sys


def solve(X: int, K: int, D: int):
    X = abs(X)
    p, now = divmod(X, D)
    if K < p:
        print(X - K * D)
        return
    K -= p
    if K % 2 == 0:
        print(now)
    else:
        print(abs(D - now))

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    solve(X, K, D)

if __name__ == '__main__':
    main()
