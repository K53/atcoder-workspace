#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    s = set(A)

    K = sorted(A + B)
    ans = []
    res = []
    for i in range(N + M):
        if K[i] in s:
            ans.append(i + 1)
        else:
            res.append(i + 1)
    print(*ans, sep=" ")
    print(*res, sep=" ")


if __name__ == '__main__':
    main()
