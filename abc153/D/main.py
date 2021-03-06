#!/usr/bin/env python3
import sys


def solve(H: int):
    num = 1
    ans = 0
    for _ in range(10 ** 12):
        ans += num
        if H == 1:
            break
        H //= 2
        num *= 2
    print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    solve(H)

if __name__ == '__main__':
    main()
