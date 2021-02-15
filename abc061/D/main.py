#!/usr/bin/env python3
import sys
INF = 10 ** 16

def main():
    N, M = map(int, input().split())
    edges = []
    costs = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a - 1, b - 1, -c))

    costs = [INF] * N
    costs[0] = 0
    for loopCount in range(N):
        for a, b, c in edges:
            if costs[a] != INF and costs[b] > costs[a] + c:
                costs[b] = costs[a] + c
                if loopCount == N - 1 and b == N - 1:
                    print("inf")
                    return

    print(-costs[N - 1])


if __name__ == '__main__':
    main()
