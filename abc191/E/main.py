#!/usr/bin/env python3
import heapq
INF = 10 ** 16
class Dijkstra():
    def __init__(self, N: int) -> None:
        self.N = N 
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((cost, toNode))
        return
    
    def build(self, startNode: int):
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [INF] * self.N
        # prev = [-1] * self.N # 経路復元する場合は移動時に直前の頂点や辺を記録して遷移していく。
        heapq.heappush(hq, (0, startNode))
        dist[startNode] = 0
        # dijkstra
        while hq:
            min_cost, now = heapq.heappop(hq)
            if min_cost > dist[now]:
                continue
            for cost, next in self.G[now]:
                if dist[next] > dist[now] + cost:
                    dist[next] = dist[now] + cost
                    # prev[next] = now # 頂点nextに至る直前の頂点を更新。
                    heapq.heappush(hq, (dist[next], next))
        return dist


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, M = map(int, input().split())
    dk = Dijkstra(N)
    for _ in range(M):
        A, B, C = map(int, input().split())
        dk.addEdge(A - 1, B - 1, C)

    for st in range(N):
        res = INF
        for nx in dk.G[st]:
            d = dk.build(nx[1]) # O(10^3)
            res = min(res, d[st] + nx[0])
        print(-1 if res == INF else res)
    return

if __name__ == '__main__':
    main()
