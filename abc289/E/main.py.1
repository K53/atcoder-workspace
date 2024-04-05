#!/usr/bin/env python3
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()
INF = 10 ** 16
        
def bfs(G: "List[to]", start_node: int) -> list:
    q = deque()
    dist = [INF] * len(G)
    q.append(start_node)
    dist[start_node] = 0
    while q:
        now = q.popleft()
        for next in G[now]:
            if dist[next] != INF:
                continue
            q.append(next)
            dist[next] = dist[now] + 1
    return dist

def main():
    T = int(input())
    for i in range(T):
        N, M = map(int, input().split())
        C = list(map(int, input().split()))
        G = [[] for _ in range(N)]
        for _ in range(M):
            u, v = map(int, input().split())
            G[u - 1].append(v - 1)
            G[v - 1].append(u - 1)
        dist = [[INF] * N for _ in range(N)]
        q = deque()
        q.append((0, N - 1))
        dist[0][N - 1] = 0
        while q:
            now_t, now_a = q.popleft()
            for next_t in G[now_t]:
                for next_a in G[now_a]:
                    if dist[next_t][next_a] != INF:
                        continue
                    if C[next_t] != C[next_a]:
                        dist[next_t][next_a] = dist[now_t][now_a] + 1
                        q.append((next_t, next_a))
        print(-1 if dist[N - 1][0] == INF else dist[N - 1][0])
    return 

if __name__ == '__main__':
    main()
