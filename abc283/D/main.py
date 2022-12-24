#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(S: str):
    from collections import deque
    az = [0] * 26
    scopes = deque()
    last = []
    for ss in S:
        if ss == "(":
            scopes.append(last)
            last = []
        elif ss == ")":
            for i in last:
                az[i] = 0
            last = scopes.pop()
        else:
            num_char = ord(ss) - ord("a")
            if az[num_char]:
                print(NO)
                return
            az[num_char] = 1
            last.append(num_char)
    print(YES)
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
