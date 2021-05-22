#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    from itertools import accumulate
    s1 = list(accumulate(A))
    s2 = list(accumulate([0] + s1))
    mostFar = list(accumulate(s1, func=max))
    ans = 0
    for nn in range(N):
        ans = max(ans, s2[nn] + mostFar[nn])
    print(ans)


if __name__ == '__main__':
    main()
