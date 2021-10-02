#!/usr/bin/env python3
import sys


def solve(N: int, K: int, D: "List[int]"):
    for i in range(N, 10000 + 1):
        if not set([int(c) for c in str(i)]) & set(D):
            print(i)
            return
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    solve(N, K, D)

if __name__ == '__main__':
    main()