#!/usr/bin/env python3
import sys


def solve(N: int):
    t = N
    ans = []
    while t > 0:
        if t % 2 == 1:
            t -= 1
            ans.append("A")
        else:
            t //= 2
            ans.append("B")
    print(*ans[::-1], sep="")
    return


# Generated by 2.8.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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