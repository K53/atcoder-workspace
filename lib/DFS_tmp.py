import sys
sys.setrecursionlimit(10 ** 9)
ans = 0
N = int(input())
class DFS():
    def __init__(self, N: int) -> None:
        self.nodes = N                          # 頂点数
        self.G = [[] for _ in range(N)]         # グラフ
        self.seen = [False] * N                 # 各ノードが訪問済みかどうかのフラグ
        self.firstOrder = []                    # ノードの行きがけ順(0-index)
        self.lastOrder = []                     # ノードの帰りがけ順(0-index)

    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int, bothDirection: bool):
        self.G[fromNode].append((toNode, cost))
        if bothDirection:
            self.G[toNode].append((fromNode, cost))
    # DFS
    def build(self, now: int, pre:int):
        sum = 0
        nonlocal ans
        # ----- ノードに到着した時の処理
        self.firstOrder.append(now)
        self.seen[now] = True
        # ----- 隣接する各ノードへの移動処理
        for next in self.G[now]:
            if self.seen[next[0]]:
                continue
            sum += self.build(next[0], now)
        # ----- ノードから戻る時の処理
        # self.lastOrder.append(now)
        sum += 1
        for t, c in self.G[now]:
            if t == pre:
                ans += sum * (self.nodes - sum) * c
        return sum

d = DFS(N)
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    d.addEdge(u - 1, v - 1, w, bothDirection=True)
d.build(0, -1)
print(ans * 2)