#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(H: int, W: int, K: int, A: "List[str]"):
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [next(tokens) for _ in range(W)]  # type: "List[str]"
    solve(H, W, K, A)

if __name__ == '__main__':
    main()
