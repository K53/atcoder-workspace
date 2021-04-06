#!/usr/bin/env python3
import sys


def solve(N: int, a: "List[int]"):
    ans = 0
    now = 1
    if not 1 in a:
        print(-1)
        return
    for i in range(N):
        if a[i] == now:
            now += 1
        else:
            ans += 1
    print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
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
