import heapq
INF = 10 ** 16
# グラフ + 座標圧縮 の問題の場合、開始点と終了点を圧縮後の座標の集合に加え忘れないこと。
class Dijkstra():
    def __init__(self, N: int) -> None:
        self.N = N 
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((cost, toNode))
        # print("Really directed Graph?")
        return

    # "toノードに到達するための辺の番号"を同時に持たせることで経路復元時にedge_numを使用できる。
    # def addEdge(self, fromNode: int, toNode: int, cost: int, edge_num: int):
    #     self.G[fromNode].append((cost, toNode, edge_num))
    #     return
    
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
                    # prev[next] = now # 頂点nextに至る直前の頂点(now)または辺(edge_num)を更新。
                    heapq.heappush(hq, (dist[next], next))
        return dist

# Usage
N = 10 ** 5 * 2 + 1
dk = Dijkstra(N)
for i in range(10 ** 5):
    dk.addEdge(2 + 2 * i, 0 + 2 * i, 2 ** i),
    dk.addEdge(1 + 2 * i, 0 + 2 * i, -2 * (2 ** i) - i),
    dk.addEdge(2 + 2 * i, 1 + 2 * i, 2 * (2 ** i) + i),

    # dk.addEdge(fromNode=a, toNode=b, cost=c)
    # dk.addEdge(fromNode=b, toNode=a, cost=c)
d = dk.build(startNode=N-1)
print(d)
"-> [0, 25, 30, 10]"