#!/usr/bin/env python3
import sys

def main():
    import heapq
    INF = 10 ** 9       # *2
    def dijkstra(edges: "List[List[(cost, to)]]", start_node: int) -> list:
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [INF] * len(edges)
        heapq.heappush(hq, (0, start_node))
        dist[start_node] = 0            # *1
        # dijkstra
        while hq:
            min_cost, now = heapq.heappop(hq)
            if min_cost > dist[now]:
                continue
            for cost, next in edges[now]:
                if dist[next] > dist[now] + cost:
                    dist[next] = dist[now] + cost
                    heapq.heappush(hq, (dist[next], next))
        return dist
    N, M, T = map(int, input().split())
    A =list(map(int, input().split()))
    G = [[] for _ in range(N)]
    rG = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        G[a - 1].append((c, b - 1))
        rG[b - 1].append((c, a - 1))
    d = dijkstra(G, 0)
    rd = dijkstra(rG, 0)
    ans = 0
    for i in range(N):
        rest = T - (d[i] + rd[i])
        if rest < 0:
            continue
        ans = max(ans, rest * A[i])
    print(ans)
    

if __name__ == '__main__':
    main()
