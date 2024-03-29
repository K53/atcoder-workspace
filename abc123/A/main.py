#!/usr/bin/env python3
import sys


def solve(a: int, b: int, c: int, d: int, e: int, k: int):
    for i in [a, b, c, d, e]:
        for j in [a, b, c, d, e]:
            if i == j:
                continue
            if abs(i - j) > k:
                print(":(")
                return
    print("Yay!")
    



# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    c = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    e = int(next(tokens))  # type: int
    k = int(next(tokens))  # type: int
    solve(a, b, c, d, e, k)

if __name__ == '__main__':
    main()
