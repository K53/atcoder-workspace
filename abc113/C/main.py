#!/usr/bin/env python3
import sys


def solve(N: int, M: int, P: "List[int]", Y: "List[int]"):
    l = [[] for _ in range(N)]
    ans = [""] * M
    num = 0
    for pp, yy in zip(P, Y):
        l[pp - 1].append((yy, num))
        num += 1
    for i in range(N):
        a = l[i]
        a.sort()
        x = 1
        for aa in a:
            pre = str(i + 1)
            post = str(x)
            ans[aa[1]] = "0" * (6 - len(pre)) + pre + "0" * (6 - len(post)) + post
            x += 1
    print(*ans, sep="\n")


    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = [int()] * (M)  # type: "List[int]"
    Y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        P[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, P, Y)

if __name__ == '__main__':
    main()
