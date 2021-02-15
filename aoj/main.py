#!/usr/bin/env python3
import sys
INF = 10 ** 9

def main():    
    V, E, r = map(int, input().split())
    edges = []
    costs = []
    for _ in range(E):
        s, t, d = map(int, input().split())
        edges.append((s, t, d))

    costs = [INF] * V
    costs[r] = 0
    for i in range(V):
        for s, t, d in edges:
            if costs[s] != INF and costs[t] > costs[s] + d:
                costs[t] = costs[s] + d
                if i == V - 1:
                    print("NEGATIVE CYCLE")
                    return
    
    for c in costs:
        print("INF" if c == INF else c)

if __name__ == '__main__':
    main()