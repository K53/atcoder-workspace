#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, S: str, T: str):
    for i in range(N):
        if S[i] == T[i]:
            continue
        if S[i] == "0" and T[i] == "o":
            continue
        if S[i] == "o" and T[i] == "0":
            continue
        if S[i] == "1" and T[i] == "l":
            continue
        if S[i] == "l" and T[i] == "1":
            continue
        print(NO)
        return
    print(YES)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    T = next(tokens)  # type: str
    solve(N, S, T)

if __name__ == '__main__':
    main()
