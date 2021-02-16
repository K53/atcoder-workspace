#!/usr/bin/env python3
import heapq
INF = 10 ** 9
# ----------------------------------------------------------------
# Input
#   1. タプル(重み, 行先)の二次元配列(隣接リスト) : 初期化時、有向無向に注意
#   2. 探索開始ノード(番号)
# Output
#   スタートから各ノードへの最小コスト
# Env
#   import heapq
#   INF = 10 ** 9
# ----------------------------------------------------------------
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
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a - 1].append((c, b - 1))
        edges[b - 1].append((c, a - 1))
    ans = INF
    for start in range(N):
        dist = dijkstra(edges, start)
        # print(dist)
        ans = min(max(dist), ans)
    print(ans)

if __name__ == '__main__':
    main()
