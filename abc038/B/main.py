#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def solve(H: "List[int]", W: "List[int]"):
    return


# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = [int()] * (2)  # type: "List[int]"
    W = [int()] * (2)  # type: "List[int]"
    for i in range(2):
        H[i] = int(next(tokens))
        W[i] = int(next(tokens))
    solve(H, W)

if __name__ == '__main__':
    main()
