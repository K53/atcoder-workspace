#!/usr/bin/env python3
import sys

def solve(N: int, A: int, B: int, C: int, D: int, E: int):
    m = min(A, B, C, D, E)
    if m > N:
        print(5)
        return
    print((N + m - 1) // m + 4)
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
    C = int(next(tokens))  # type: int
    D = int(next(tokens))  # type: int
    E = int(next(tokens))  # type: int
    solve(N, A, B, C, D, E)

if __name__ == '__main__':
    main()
