#!/usr/bin/env python3
import heapq
INF = 10 ** 9
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

def main():
    n, k = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(k):
        i = list(map(int, input().split()))
        if i[0] == 1:
            edge[i[1] - 1].append((i[3], i[2] - 1))
            edge[i[2] - 1].append((i[3], i[1] - 1))
        else:
            costs = dijkstra(edge ,i[1] - 1)
            print(-1 if costs[i[2] - 1] == INF else costs[i[2] - 1])
    return
if __name__ == '__main__':
    main()