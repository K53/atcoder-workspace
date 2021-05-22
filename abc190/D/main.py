#!/usr/bin/env python3
import sys

def getDivisors(n: int):
    d = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            d += 1
            if i != n // i:
                d += 1
        i += 1
    return d

def solve(N: int):
    while N % 2 == 0:
        N //= 2
    d = getDivisors(N)
    print(d * 2)

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
