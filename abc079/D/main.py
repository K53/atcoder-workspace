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
    H, W = map(int, input().split())
    edges = [[] for i in range(10)]
    for i in range(10):
        c = list(map(int, input().split()))
        for j in range(10):
            if i == j:
                continue
            edges[i].append((c[j], j))
    nums = [0] * 10
    for _ in range(H):
        A = list(map(int, input().split()))
        for a in A:
            if a == -1:
                continue
            nums[a] += 1
    ans = 0
    for i, s in enumerate(nums):
        if i == 1:
            continue
        dist = dijkstra(edges, i)
        ans += dist[1] * s
    print(ans)

if __name__ == '__main__':
    main()
