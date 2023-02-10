#!/usr/bin/env python3
import sys


def solve(S: str):
    for i in range(len(S) - 1):
        l = len(S[:(-1-i)])
        if l % 2 == 1:
            continue
        if S[:(-1-i)][:(l // 2)] == S[(l // 2):(-1-i)]:
            print(len(S) - i - 1)
            return
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    S = next(tokens)  # type: str
    solve(S)

if __name__ == '__main__':
    main()
