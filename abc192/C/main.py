#!/usr/bin/env python3
import sys

def g2(n):
    l = sorted(list(map(int, str(n))))
    return int("".join(map(str, l)))

def g1(n):
    l = sorted(list(map(int, str(n))), reverse=True)
    return int("".join(map(str, l)))

def solve(N: int, K: int):
    n = N
    for i in range(K):
        n = g1(n) - g2(n)
    print(n)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()
