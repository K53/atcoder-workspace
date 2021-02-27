#!/usr/bin/env python
import heapq
INF = 10 ** 16

def dijkstra(edges: "List[List[(cost, departure, to)]]", start_node: int) -> list:
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
        for cost, departure, next in edges[now]:
            rest = 0 if min_cost % departure == 0 else departure - min_cost % departure
            if dist[next] > dist[now] + cost + rest:
                dist[next] = dist[now] + cost + rest
                heapq.heappush(hq, (dist[next], next))
    return dist

def main():
    N, M, K = map(int, input().split())
    t = [0] + [int(input()) for _ in range(N - 2)] + [0]
    edges = [[] for _ in range(N)]
    for i in range(M):
        a, b, c, d = map(int, input().split())
        edges[a - 1].append((c + t[b - 1], d, b - 1))
        edges[b - 1].append((c + t[a - 1], d, a - 1))
    d = dijkstra(edges, 0)
    print(d[N - 1] if d[N - 1] <= K else -1)

if __name__ == '__main__':
    main()
