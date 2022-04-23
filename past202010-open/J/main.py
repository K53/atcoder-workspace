#!/usr/bin/env python3

def main():
    N, M = map(int, input().split())
    Xab, Xac, Xbc =  map(int, input().split())
    S = input()
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
        
        def build(self, startNode: int):
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
                for cost, next in self.G[now]:
                    if dist[next] > dist[now] + cost:
                        dist[next] = dist[now] + cost
                        heapq.heappush(hq, (dist[next], next))
            return dist

    # N     Ain
    # N+1   Bin
    # N+2   Cin
    # N+3   Aout
    # N+4   Bout
    # N+5   Cout
    dk = Dijkstra(N + 6)
    for _ in range(M):
        aa, bb, cc = map(int, input().split())
        dk.addEdge(aa - 1, bb - 1, cc)
        dk.addEdge(bb - 1, aa - 1, cc)
    
    for i in range(N):
        if S[i] == "A":
            dk.addEdge(i, N, 0)
            dk.addEdge(N + 3, i, 0)
        elif S[i] == "B":
            dk.addEdge(i, N + 1, 0)
            dk.addEdge(N + 4, i, 0)
        else:
            dk.addEdge(i, N + 2, 0)
            dk.addEdge(N + 5, i, 0)
    dk.addEdge(N, N + 4, Xab)
    dk.addEdge(N, N + 5, Xac)
    dk.addEdge(N + 1, N + 3, Xab)
    dk.addEdge(N + 1, N + 5, Xbc)
    dk.addEdge(N + 2, N + 3, Xac)
    dk.addEdge(N + 2, N + 4, Xbc)

    d = dk.build(startNode=0)
    print(d[N - 1])
    return

if __name__ == '__main__':
    main()
