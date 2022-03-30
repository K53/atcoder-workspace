#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    c = []
    for i in range(N):
        if S[i] == "A":
            c.append("B")
            c.append("B")
        else:
            c.append(S[i])
    ans = []
    skip = 0
    # print(c)
    for i in range(len(c)):
        if skip:
            skip = 0
            # print(ans ,i)
            continue
        if i + 1 < len(c) and c[i] == c[i + 1] == "B":
            ans.append("A")
            skip = 1
            # print(ans ,i)
        else:
            ans.append(c[i])
    print(*ans, sep="")
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
    solve(N, S)

if __name__ == '__main__':
    main()
