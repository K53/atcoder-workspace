#!/usr/bin/env python3
import sys


def solve(A: int, B: int):
    sa = str(A)
    sb = str(B)
    a, b = 0, 0
    for i in range(3):
        a += int(sa[i])
        b += int(sb[i])
    print(max(a, b))
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(A, B)

if __name__ == '__main__':
    main()
