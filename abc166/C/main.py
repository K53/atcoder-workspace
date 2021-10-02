#!/usr/bin/env python3
import sys

def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    a, b = [], []
    for _ in range(M):
        aa, bb = map(int, input().split())
        a.append(aa)
        b.append(bb)
    nodes = [[] for _ in range(N)]
    for i in range(M):
        nodes[a[i] - 1].append(b[i] - 1)
        nodes[b[i] - 1].append(a[i] - 1)
    ans = 0
    for v in range(N):
        for i in nodes[v]:
            if H[v] <= H[i]:
                break
        else:
            ans += 1
    print(ans)
    return





if __name__ == '__main__':
    main()
