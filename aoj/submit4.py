#!/usr/bin/env python3
import sys

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0563&lang=jp

def main():
    import statistics
    W, H = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    xpoints = []
    ypoints = []
    for _ in range(N):
        x, y = map(int, sys.stdin.readline().split())
        xpoints.append(x)
        ypoints.append(y)
    xss = [statistics.median_low(xpoints), statistics.median_high(xpoints)]
    yss = [statistics.median_low(ypoints), statistics.median_high(ypoints)]
    maxd = 0
    ansd = 10 ** 16
    ansx = 0
    ansy = 0
    for xs in xss:
        for ys in yss:
            sumd = 0
            for x, y in zip(xpoints, ypoints):
                d = abs(x - xs) + abs(y - ys)
                sumd += d * 2
                maxd = max(maxd, d)
            # ansd == sumd - maxdのケースも更新すると、x軸y軸方向に最小にならなくなるので無視
            if ansd > sumd - maxd:
                ansx = xs
                ansy = ys
                ansd = sumd - maxd
    print(ansd)
    print(ansx, ansy)
    return

if __name__ == '__main__':
    main()