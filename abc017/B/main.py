#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(X: str):
    N = len(X)
    num = 0
    X += "u"
    while num < N:
        if X[num] in "oku":
            num += 1
            continue
        if X[num] == "c" and X[num + 1] == "h":
            num += 2
            continue
        print(NO)
        return
    print(YES)
    return


# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = next(tokens)  # type: str
    solve(X)

if __name__ == '__main__':
    main()
