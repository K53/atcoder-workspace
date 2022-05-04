#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    l = [0] * N
    for aa in A:
        l[aa - 1] += 1
    q = []
    w = []
    for i, ll in enumerate(l):
        if ll == 0:
            q.append(i)
        if ll > 1:
            for _ in range(ll - 1):
                w.append(i)
    ans = 0
    for qq, ww in zip(q, w):
        ans += abs(qq - ww)
    print(ans)
    return

if __name__ == '__main__':
    main()