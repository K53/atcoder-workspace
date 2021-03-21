#!/usr/bin/env python3
import sys

def getDivisors(n: int):
    # validation check
    if not isinstance(n, int):
        raise("[ERROR] parameter must be integer")
    if n < 0:
        raise("[ERROR] parameter must be not less than 0 (n >= 0)")

    Divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            Divisors.append((i, n//i))
        i += 1
    return Divisors

def solve(N: int):
    l = getDivisors(N)
    ans = 10 ** 13
    for x, y in l:
        ans = min(ans, x + y - 2)
    print(ans)
    return


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
