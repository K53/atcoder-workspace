#!/usr/bin/env python3


def main():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        ka = list(map(int, input().split()))
        A.append(ka[1:])
    P, Q = map(int, input().split())
    B = set(map(int, input().split()))
    ans = 0
    for aa in A:
        same = set(aa) & B
        if len(same) >= Q:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
