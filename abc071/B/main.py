#!/usr/bin/env python3
import sys


def solve(S: str):
    import string
    ans = set(string.ascii_lowercase) -  set(S)
    l = list(ans)
    l.sort()
    if len(l) == 0:
        print("None")
    else:
        print(l[0])
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
