#!/usr/bin/env python3
import heapq
INF = 10 ** 9

def dijkstras(edges: "List[List[(cost, to)]]", start: "(cost, to)"):
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    for cost, to in edges[start]:
        heapq.heappush(hq, (cost, to))
        dist[to] = min(cost, dist[to])
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
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a - 1].append((c, b - 1))
    
    for start in range(N):
        # set start info
        dist = dijkstras(edges, start)
        print(-1 if dist[start] == INF else dist[start])
    return

if __name__ == '__main__':
    main()
