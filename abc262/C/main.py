#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    ans = 0
    c = 0
    for i in range(N):
        if a[i] == i + 1:
            ans += 1
        else:
            if a[a[i] - 1] == i + 1:
                c += 1
    print((ans * (ans - 1) // 2) + c // 2)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
