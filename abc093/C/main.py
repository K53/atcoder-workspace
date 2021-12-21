#!/usr/bin/env python3
import sys


def solve(A: int, B: int, C: int):
    mm = max(A, B, C)
    A = mm - A
    B = mm - B
    C = mm - C
    ans, qq = 0, 0
    for i in [A, B, C]:
        p, q = divmod(i, 2)
        ans += p
        qq += q
    if qq == 1:
        ans += 2
    elif qq == 2:
        ans += 1
    print(ans)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    solve(A, B, C)

if __name__ == '__main__':
    main()