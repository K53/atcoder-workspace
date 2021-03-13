#!/usr/bin/env python3
import sys
from collections import defaultdict


def main():
    d = defaultdict(lambda: 0)
    N = int(input())
    for _ in range(N):
        s = input()
        d[s] += 1
    l = []
    for k, v in d.items():
        l .append((v, k))
    l.sort(reverse=True)
    a = l[0][0]
    ans = []
    for v, k in l:
        if v < a:
            break
        ans.append(k)
    ans.sort()
    print(*ans, sep="\n")
    return




if __name__ == '__main__':
    main()
