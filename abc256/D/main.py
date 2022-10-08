#!/usr/bin/env python3
import sys


def solve(N: int, L: "List[int]", R: "List[int]"):
    imos = [0] * (2 * 10 ** 5 + 1)
    for ll, rr in zip(L, R):
        imos[ll] += 1
        imos[rr] -= 1
    acc = [0]
    for i in range(2 * 10 ** 5 + 1):
        acc.append(acc[-1] + imos[i])
    acc = acc[1:]
    now = -1
    ans = []
    for i in range(2 * 10 ** 5 + 1):
        if now == -1:
            if acc[i] != 0:
                now = i
        else:
            if acc[i] == 0:
                ans.append((now, i))
                now = -1
    for aa in ans:
        print(*aa, sep=" ")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int()] * (N)  # type: "List[int]"
    R = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
    solve(N, L, R)

if __name__ == '__main__':
    main()