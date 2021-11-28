#!/usr/bin/env python3
import sys


def solve(N: int, P: int):
    def primeFactorise(n: int) -> list:
        primeFactors = []
        i = 2
        while i * i <= n: # sqrt(N)まで試し割りする。
            exp = 0
            while n % i == 0:
                exp += 1
                n //= i
            if exp != 0:
                primeFactors.append((i, exp))
            i += 1
        if n != 1:
            primeFactors.append((n, 1))
        return primeFactors

    l = primeFactorise(P)
    ans = 1
    for num, i in l:
        k = i // N
        if k != 0:
            ans *= num ** k
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
    P = int(next(tokens))  # type: int
    solve(N, P)

if __name__ == '__main__':
    main()
