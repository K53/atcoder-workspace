#!/usr/bin/env python3
import sys


def solve(S: int, K: int):
    num = 0
    last = 1
    for i in str(S):
        if i != "1":
            last = i
            break
        num += 1
    if num >= K:
        print(1)
    else:
        print(last)
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(S, K)

if __name__ == '__main__':
    main()
