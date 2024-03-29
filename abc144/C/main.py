#!/usr/bin/env python3
import sys
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

def solve(N: int):
    l = getDivisors(N)
    ans = 10 ** 16
    for i in range(len(l)):
        ans = min(ans, l[i] + l[len(l) - 1 - i] - 2)
        if i == len(l) - 1 - i:
            break
    print(ans)
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
