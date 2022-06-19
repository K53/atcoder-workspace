#!/usr/bin/env python3
import sys
import itertools
MOD = 998244353  # type: int

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(itertools.accumulate(A))
    C = list(itertools.accumulate(B))
    D = list(itertools.accumulate(C))
    acc = list(itertools.accumulate(range(1, N + 2)))
    qs = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            qs.append((query[1], query[2], query[0]))
        else:
            qs.append((query[1], query[0]))

    qs.sort()
    print(qs)
    for query in qs:
        if query[-1] == 1:
            x, v = query[1], query[0]
        else:
            x = query[0]
    return

if __name__ == '__main__':
    main()

