#!/usr/bin/env python3
import sys
import heapq
INF = 10 ** 16
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
    n, m, s, t = map(int, input().split())
    yen_edges = [[] for _ in range(n)]
    snuuk_edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        yen_edges[v - 1].append((a, u - 1))
        yen_edges[u - 1].append((a, v - 1))
        snuuk_edges[v - 1].append((b, u - 1))
        snuuk_edges[u - 1].append((b, v - 1))
    yd = dijkstra(yen_edges, s - 1)
    sd = dijkstra(snuuk_edges, t - 1)
    cost_min = INF
    ans = []
    for i in reversed(range(n)):
        cost_via_i = yd[i] + sd[i]
        cost_min = min(cost_min, cost_via_i)
        ans.append(10 ** 15 - cost_min)
    print(*reversed(ans), sep="\n")
        
if __name__ == '__main__':
    main()
