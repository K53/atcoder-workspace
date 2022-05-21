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
#   O(V + ElogE) <- これが正しいかも https://atcoder.jp/contests/past202107-open/editorial/2205
# Note
#   *1 https://atcoder.jp/contests/abc191/tasks/abc191_e 
#       - 多始点ダイクストラの場合の注意。
#       - コストの異なる並行な辺がある場合、小さい方を選択する必要あり。 ？【未調査】
#       - dist[start_node] = min(cost, dist[start_node])
#   *2 https://atcoder.jp/contests/tkppc4-1/tasks/tkppc4_1_h
#       - INFの値は毎回吟味すること。
# verify
# - https://atcoder.jp/contests/abc214/tasks/abc214_c (グラフ)
# - https://atcoder.jp/contests/past201912-open/tasks/past201912_j (グリッド)
# - https://atcoder.jp/contests/abc164/tasks/abc164_e (拡張ダイクストラ)
# ------------------------------------------------------------------------------

#  グラフ
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
        print("Really directed Graph?")
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

# Usage
N = 4
dk = Dijkstra(N)
for a, b, c in [(0, 3, 10), (1, 2, 10), (2, 3, 20), (1, 3, 15)]:
    dk.addEdge(a, b, c)
    dk.addEdge(b, a, c)
d = dk.build(startNode=0)
print(d)
"-> [0, 25, 30, 10]"

# グリッド
import heapq
INF = 10 ** 16
class Dijkstra():
    def __init__(self, H: int, W: int, G: "list[list[int]]") -> None:
        self.H = H
        self.W = W
        self.G = G
        return
    
    def build(self, startY: int, startX: int):
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [[INF for _ in range(self.W)] for _ in range(self.H)]
        heapq.heappush(hq, (0, startY, startX)) # (cost, y, x)
        dist[startY][startX] = 0
        # dijkstra
        while hq:
            min_cost, nowy, nowx = heapq.heappop(hq)
            if min_cost > dist[nowy][nowx]:
                continue
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= self.H or nextx >= self.W:
                    continue
                cost = self.G[nexty][nextx]
                if dist[nexty][nextx] > dist[nowy][nowx] + cost:
                    dist[nexty][nextx] = dist[nowy][nowx] + cost
                    heapq.heappush(hq, (dist[nexty][nextx], nexty, nextx))
        return dist

# Usage
H = 5
W = 6
Grid = [
    [9, 9, 9, 9, 1, 0],
    [9, 9, 9, 9, 1, 9],
    [9, 9, 9, 1, 1, 1],
    [9, 1, 1, 1, 9, 1],
    [0, 1, 9, 9, 9, 0]
]
dk = Dijkstra(H, W, Grid)
d = dk.build(startY=0, startX=0)
print(d)
"""
-> [36, 29, 26, 17, 8, 8]
[27, 20, 21, 14, 7, 16]
[18, 11, 12, 5, 6, 7]
[9, 2, 3, 4, 13, 8]
[0, 1, 10, 13, 17, 8]
"""

# 拡張ダイクストラ (頂点倍加)
# ビルド時に状態遷移の分とノード移動分を別で考慮する。
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
        print("Really directed Graph?")
        return
        
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