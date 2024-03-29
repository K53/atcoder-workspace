#!/usr/bin/env python3
import sys
import math

def solve(a: int, b: int, d: int):
    c = math.radians(d)
    X = math.cos(c) * a - math.sin(c) * b
    Y = math.sin(c) * a + math.cos(c) * b
    print(X, Y)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    d = int(next(tokens))  # type: int
    solve(a, b, d)

if __name__ == '__main__':
    main()
