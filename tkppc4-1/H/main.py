#!/usr/bin/env python
import heapq
INF = 10 ** 16

class Dijkstra():
    def __init__(self, N: int) -> None:
        self.N = N 
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int, time: int):
        self.G[fromNode].append((cost, time, toNode))
    
    def build(self, startNode: int, T: list):
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [INF] * self.N
        heapq.heappush(hq, (0, startNode))
        dist[startNode] = 0
        # dijkstra
        while hq:
            min_cost, now = heapq.heappop(hq)
            if min_cost > dist[now]:
                continue
            for cost, time, next in self.G[now]:
                wait = (0 + T[next]) if min_cost % time == 0 else ((time - min_cost % time) + T[next])
                if dist[next] > dist[now] + cost + wait:
                    dist[next] = dist[now] + cost + wait
                    heapq.heappush(hq, (dist[next], next))
        return dist


def main():
    N, M, K = map(int, input().split())
    T = [0] + [int(input()) for _ in range(1, N - 1)] + [0]
    dk = Dijkstra(N)
    for _ in range(M):
        a, b, c, d = map(int, input().split())
        dk.addEdge(a - 1, b - 1, c, d)
        dk.addEdge(b - 1, a - 1, c, d)
    dist = dk.build(0, T)
    ans = dist[N - 1]
    print(ans if ans != INF and ans <= K else -1)
    return

if __name__ == '__main__':
    main()
