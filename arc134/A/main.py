#!/usr/bin/env python3
import sys


def solve(N: int, L: int, W: int, a: "List[int]"):
    next = 0
    a.sort()
    ans = 0
    for aa in a:
        if next < aa:
            p, q = divmod(aa - next, W)
            if q > 0:
                p += 1
            ans += p
        next = aa + W
        if next > L:
            break
        # print(next, ans)
    p, q = divmod(L - next, W)
    # print(p, q)
    if q > 0:
        p += 1
    ans += p
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L, W, a)

if __name__ == '__main__':
    main()