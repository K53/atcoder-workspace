#!/usr/bin/env python3
import sys


def solve(abc: int):
    s = str(abc)
    a1 = int(s[1] + s[2] + s[0])
    a2 = int(s[2] + s[0] + s[1])
    print(abc + a1 + a2)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    abc = int(next(tokens))  # type: int
    solve(abc)

if __name__ == '__main__':
    main()
