#!/usr/bin/env python3
import sys


def solve(N: int):
    count = 0
    for num in range(1, 10 ** 6 + 1):
        s = str(num)
        t = int(s + s)
        if t > N:
            break
        count += 1

    print(count)
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
