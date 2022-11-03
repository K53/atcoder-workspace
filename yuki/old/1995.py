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

def main():
    N, M = map(int, input().split())
    A, B = [], []
    city = set()
    for i in range(M):
        aa, bb = map(int, input().split())
        A.append(aa)
        B.append(bb)
        city.add(aa)
        city.add(bb)
    compressed = {}
    compressed_to_raw = []
    city.add(1) # 開始と終了を忘れないこと
    city.add(N)
    city = sorted(list(city))
    for index, val in enumerate(city):
        compressed[val] = index
        compressed_to_raw.append(val)
    dk = Dijkstra(len(city))
    for i in range(len(city) - 1):
        aa = city[i]
        bb = city[i + 1]
        s = compressed[aa]
        t = compressed[bb]
        d = (bb - aa) * 2
        dk.addEdge(s, t, d)
    for aa, bb in zip(A, B):
        s = compressed[aa]
        t = compressed[bb]
        d = 2 * bb - 2 * aa - 1
        dk.addEdge(s, t, d)
    res = dk.build(startNode=0)
    print(res[-1])
    return


if __name__ == '__main__':
    main()