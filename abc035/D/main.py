#!/usr/bin/env python3
import sys
import heapq
INF = 10 ** 9

def dijkstra(edges: "List[List[(cost, to)]]", start_node: int) -> list:
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    heapq.heappush(hq, (0, start_node))
    dist[start_node] = 0
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

def main():
    N, M, T = map(int, input().split())
    A =list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    edges_inv = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a - 1].append((c, b - 1))
        edges_inv[b - 1].append((c, a - 1))
    
    cost1 = dijkstra(edges, 0)
    cost2 = dijkstra(edges_inv, 0)
    ans = 0
    for i in range(N):
        cost = cost1[i] + cost2[i]
        if T - cost < 0:
            continue
        ans = max(ans, (T - cost) * A[i])
    print(ans)

if __name__ == '__main__':
    main()
