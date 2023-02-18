#!/usr/bin/env python3

MOD = 2  # type: int


def main():
    N, M = map(int, input().split())
    k = []
    s = []
    for _ in range(M):
        ks = list(map(int, input().split()))
        k.append(ks[0])
        s.append(set(ks[1:]))
    p = list(map(int, input().split()))
    ans = 0
    for i in range(2 ** N):
        ons = [0] * M
        for b in range(N):
            if (i >> b) & 1:
                for d in range(M):
                    if b + 1 in s[d]:
                        ons[d] += 1
                        ons[d] %= 2
        if p == ons:
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
