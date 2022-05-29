#!/usr/bin/env python3
from math import gcd
import sys


def solve(N: int, A: int, B: int):
    AB = A * B // gcd(A, B)

    # k
    aa = (N - A) // A + 1
    bb = (N - B) // B + 1
    ab = (N - AB) // AB + 1

    numA = (aa * (2 * A + (aa - 1) * A)) // 2
    numB = (bb * (2 * B + (bb - 1) * B)) // 2
    numAB = (ab * (2 * AB + (ab - 1) * AB)) // 2

    total = (N * (2 + (N - 1))) // 2

    print(total - (numA + numB - numAB))


    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(N, A, B)

if __name__ == '__main__':
    main()
