#!/usr/bin/env python3
import sys


def solve(N: int):
    def getDivisors(n: int):
        lowerDivisors, upperDivisors = [], []
        i = 1
        while i * i <= n: # sqrt(N)まで試し割りする。
            if n % i == 0:
                lowerDivisors.append(i)
                if i != n // i:
                    upperDivisors.append(n//i)
            i += 1
        return lowerDivisors + upperDivisors[::-1]

    print(*getDivisors(N), sep="\n")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
