#!/usr/bin/env python3
import sys


def solve(K: int, D: "List[List[int]]"):
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    K = int(next(tokens))  # type: int
    D = [[int(next(tokens)) for _ in range(K)] for _ in range(K)]  # type: "List[List[int]]"
    solve(K, D)

if __name__ == '__main__':
    main()
