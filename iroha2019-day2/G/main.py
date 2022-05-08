#!/usr/bin/env python3
import sys
import heapq
INF = 10 ** 16
class Dijkstra():
    def __init__(self, N: int, K: int) -> None:
        self.N = N 
        self.K = K
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((cost, toNode))
    
    def build(self, startNode: int, flower_init: int, X: list, Y: list):
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [[INF] * (self.K + 1) for _ in range(self.N)]
        heapq.heappush(hq, (0, startNode, flower_init))
        dist[startNode][flower_init] = 0
        # dijkstra
        while hq:
            min_cost, node_now, flower_now = heapq.heappop(hq)
            if min_cost > dist[node_now][flower_now]:
                continue

            # State Change
            flower_next = flower_now + X[node_now]
            if flower_next < self.K + 1:
                for i in range(flower_next + 1):
                    if dist[node_now][i] > min_cost + Y[node_now]:
                        dist[node_now][i] = min_cost + Y[node_now]
                        heapq.heappush(hq, (dist[node_now][i], node_now, i))

            # Move Node
            for cost, node_next in self.G[node_now]:
                if dist[node_next][flower_now] > dist[node_now][flower_now] + cost:
                    dist[node_next][flower_now] = dist[node_now][flower_now] + cost
                    heapq.heappush(hq, (dist[node_next][flower_now], node_next, flower_now))
        return dist


def main():
    N, M, K = map(int, input().split())
    dk = Dijkstra(N, K)
    for _ in range(M):
        a, b, c = map(int, input().split())
        dk.addEdge(fromNode=a-1, toNode=b-1, cost=c)
        dk.addEdge(fromNode=b-1, toNode=a-1, cost=c)

    X, Y = [], []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    dist = dk.build(0, 0, X, Y)
    ans = dist[N - 1][K]
    print(ans if ans != INF else -1)
    
if __name__ == '__main__':
    main()
