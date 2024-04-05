#!/usr/bin/env python3
import sys
INF = 10 ** 18
def input():
    return sys.stdin.readline()[:-1]

def dfs(edges: "List[to]", counter: "List[count]", start_node: int) -> list:
    s = []
    dist = [INF] * len(edges)
    dist[start_node] = 0
    s.append(start_node)
    while not len(s) == 0:
        now = s.pop()
        for next in edges[now]:
            if dist[next] != INF:
                continue
            s.append(next)
            dist[next] = dist[now] + 1
            counter[next] += counter[now]
    return

def main():
    N, Q = map(int, input().split())
    counter = [0] * N
    g = []
    for _ in range(N):
        g.append([])
    for _ in range(N - 1):
        a, b = map(lambda i: int(i) - 1, input().split())
        g[a].append(b)
        g[b].append(a)
    for i in range(Q):
        p, x = map(int, input().split())
        counter[p - 1] += x
    
    dfs(g, counter, 0)
    print(*counter, sep=" ")

if __name__ == '__main__':
    main()
