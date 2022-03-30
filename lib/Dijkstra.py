# ------------------------------------------------------------------------------
#     ダイクストラ
# ------------------------------------------------------------------------------
# 解説
# - 移動可能なノードのうち、最も低コストなものから更新していく。
# - すでに移動先のノードにより低コストな経路が見つかっている場合は更新しない。
# - 各ノードの最短経路を出力する。
# 
# 条件
# - コスト負の辺を含まない。→ 含む場合はベルマンフォート法(bellmanFord)を使用。
# 
# Order
#   O((V + E) * logV)
# Note
#   *1 https://atcoder.jp/contests/abc191/tasks/abc191_e 
#       - 多始点ダイクストラの場合の注意。
#       - コストの異なる並行な辺がある場合、小さい方を選択する必要あり。 ？【未調査】
#       - dist[start_node] = min(cost, dist[start_node])
#   *2 https://atcoder.jp/contests/tkppc4-1/tasks/tkppc4_1_h
#       - INFの値は毎回吟味すること。
# verify
# - https://atcoder.jp/contests/abc214/tasks/abc214_c
# ------------------------------------------------------------------------------
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

# Usage
N = 4
dk = Dijkstra(N)
for a, b, c in [(0, 3, 10), (1, 2, 10), (2, 3, 20), (1, 3, 15)]:
    dk.addEdge(a, b, c)
    dk.addEdge(b, a, c)
d = dk.build(startNode=0)
print(d)
"-> [0, 25, 30, 10]"




# 旧ダイクストラ
# ----------------------------------------------------------------
# Input
#   1. タプル(重み, 行先)の二次元配列(隣接リスト)
#   2. 探索開始ノード(番号)
# Output
#   スタートから各ノードへの最小コスト
# ----------------------------------------------------------------
# import heapq
# INF = 10 ** 9       # *2
# def dijkstra(edges: "List[List[(cost, to)]]", start_node: int) -> list:
#     hq = []
#     heapq.heapify(hq)
#     # Set start info
#     dist = [INF] * len(edges)
#     heapq.heappush(hq, (0, start_node))
#     dist[start_node] = 0            # *1
#     # dijkstra
#     while hq:
#         min_cost, now = heapq.heappop(hq)
#         if min_cost > dist[now]:
#             continue
#         for cost, next in edges[now]:
#             if dist[next] > dist[now] + cost:
#                 dist[next] = dist[now] + cost
#                 heapq.heappush(hq, (dist[next], next))
#     return dist