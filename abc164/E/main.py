#!/usr/bin/env python3
import sys
import heapq
SILVER_MAX = 2500
INF = 10 ** 16
class Dijkstra():
    def __init__(self, N: int) -> None:
        self.N = N 
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, time_cost: int, silver_cost: int):
        self.G[fromNode].append((time_cost, silver_cost, toNode))
    
    def build(self, startNode: int, silver_init: int, C: list, D: list):
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [[INF] * (SILVER_MAX + 1) for _ in range(self.N)]
        heapq.heappush(hq, (0, startNode, silver_init))
        dist[startNode][silver_init] = 0
        # dijkstra
        while hq:
            min_time_cost, node_now, silver_now = heapq.heappop(hq)
            if min_time_cost > dist[node_now][silver_now]:
                continue

            # State Change
            silver_next = silver_now + C[node_now]
            if silver_next < SILVER_MAX:
                if dist[node_now][silver_next] > dist[node_now][silver_now] + D[node_now]:
                    dist[node_now][silver_next] = dist[node_now][silver_now] + D[node_now]
                    heapq.heappush(hq, (dist[node_now][silver_next], node_now, silver_next))

            # Move Node
            for time_cost, silver_cost, node_next in self.G[node_now]:
                silver_next = silver_now - silver_cost
                if silver_next < 0:
                    continue
                if dist[node_next][silver_next] > dist[node_now][silver_now] + time_cost:
                    dist[node_next][silver_next] = dist[node_now][silver_now] + time_cost
                    heapq.heappush(hq, (dist[node_next][silver_next], node_next, silver_next))
        return dist

def main():
    N, M, S = map(int, input().split())
    init_silver = min(S, SILVER_MAX)

    dk = Dijkstra(N)
    for _ in range(M):
        u, v, a, b = map(int, input().split())
        dk.addEdge(u - 1, v - 1, b, a)
        dk.addEdge(v - 1, u - 1, b, a)

    C, D = [], []
    for _ in range(N):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    dist = dk.build(0, init_silver, C, D)
    for i in range(1, N):
        print(min(dist[i]))

if __name__ == '__main__':
    main()
