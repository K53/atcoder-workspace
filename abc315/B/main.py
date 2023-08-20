#!/usr/bin/env python3
import sys


def solve(M: int, D: "List[int]"):
    hv = sum(D) // 2 + 1
    for i in range(M):
        if hv > D[i]:
            hv -= D[i]
        else:
            print(i + 1, hv)
            return
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    M = int(next(tokens))  # type: int
    D = [int(next(tokens)) for _ in range(M)]  # type: "List[int]"
    solve(M, D)

if __name__ == '__main__':
    main()
