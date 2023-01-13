#!/usr/bin/env python3
import sys
import bisect

def main():
    N, M = map(int, input().split())
    p = [int(input()) for _ in range(N)] + [0]
    ps = set()
    for i in range(len(p)):
        for j in range(len(p)):
            ps.add(p[i] + p[j])
    ps = sorted(list(ps))
    ans = 0
    for i in ps:
        rest = M - i
        if rest < 0:
            continue
        idx = bisect.bisect_right(ps, rest)
        if idx == 0:
            # print(i)
            ans = max(ans, i)
        else:
            # print(i, ps[idx - 1])
            ans = max(ans, i + ps[idx - 1])
    print(ans)
    return


if __name__ == '__main__':
    main()
