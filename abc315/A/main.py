#!/usr/bin/env python3
import sys


def solve(S: str):
    ng = set("a,e,i,o,u".split(","))
    ans = []
    for ss in S:
        if ss in ng:
            continue
        ans.append(ss)
    print(*ans, sep="")
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
