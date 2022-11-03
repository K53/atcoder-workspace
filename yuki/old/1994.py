#!/usr/bin/env python3
from collections import defaultdict
INF = 10 ** 16

def main():
    N = int(input())
    d = defaultdict(int)
    names = []
    for i in range(N):
        name = input()
        names.append(name)
        for i in range(len(name)):
            g = name[:i] + "*" + name[(i + 1):]
            d[g] += 1
    for name in names:
        ans = -len(name)
        for i in range(len(name)):
            g = name[:i] + "*" + name[(i + 1):]
            ans += d[g]
        print(ans)
    return


if __name__ == '__main__':
    main()