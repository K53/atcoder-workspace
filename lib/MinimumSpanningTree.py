# 最小全域木自体(具体的にどのノードとどのノードが繋がれてるか)を生成する必要がある場合
#   -> クラスカル法
#
# それいがいはどちらも一緒。
#
# ### NOTE: 2023/02時点でのライブラリ間の相違


# ------------------------------------------------------------------------------
#     最小全域木(クラスカル法)
# ------------------------------------------------------------------------------
# 解説
# - コスト最小の辺から順に貪欲に見て行き、木に加えると閉路を作ってしまう場合には捨てる。
# - そうでないなら木に加える。
# 
# リンク
# - https://dai1741.github.io/maximum-algo-2012/docs/minimum-spanning-tree/
# - https://www.momoyama-usagi.com/entry/math-risan13
# 
# 計算量
# - O(ElogV) : 辺の数Eに依存。UnionFindはα(n)であるためほぼ定数となり、
# - 辺のソートが支配的になる。
# 
# verify
# - https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f?lang=ja
# - https://atcoder.jp/contests/abc218/tasks/abc218_e
# - https://atcoder.jp/contests/abc228/tasks/abc228_c
# ------------------------------------------------------------------------------
from UnionFind import UnionFind

class Kruskal():
    def __init__(self, N: int) -> None:
        # self.minimumG = [[] for _ in range(N)] # 全域最小木自体が欲しい場合にはこれを有効にする。
        self.edges = []
        self.uf =  UnionFind(N)
        self.minimunCost = 0 # 最小全域木を構成する全体のコストの総和の最小。
        return
    
    def addEdge(self, a: int, b: int, cost: int):
        self.edges.append((cost, a, b))
        return
    
    def build(self):
        for cost, a, b in sorted(self.edges):
            if self.uf.same(a, b):
                continue
            self.minimunCost += cost
            self.uf.union(a, b)
            # --- 全域最小木自体を構築 ---
            # self.minimumG[a].append(b)
            # self.minimumG[b].append(a)
        return self.minimunCost

# ------------------------------------------------------------------------------
#     最小全域木(プリム法)
# ------------------------------------------------------------------------------
# 解説
# - ダイクストラ様に探索。
# - 任意の頂点から移動可能な辺の中で追加しても閉路を作らず、最小コストのものを追加。
#
# 注意
# - 現状は最小全域木自体の構築は未実装。
# 
# リンク
# - https://tjkendev.github.io/procon-library/python/graph/min_st_prim.html
# 
# 計算量
# - O(ElogV)
# 
# vodify
# - https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_f?lang=ja
# - https://atcoder.jp/contests/abc065/tasks/arc076_b
# ------------------------------------------------------------------------------
import heapq
class Prim():
    def __init__(self, N: int) -> None:
        self.G = [[] for _ in range(N)]
        self.seen = [[] for _ in range(N)]
        self.minimunCost = 0 # 最小全域木を構成する全体のコストの総和の最小。
        return
    
    def addEdge(self, a: int, b: int, cost: int):
        self.G[a].append((cost, b))
        self.G[b].append((cost, a))
        return

    def build(self):
        hq = []
        heapq.heapify(hq)
        start_node = 0
        heapq.heappush(hq, (0, start_node))
        while hq:
            min_cost, now = heapq.heappop(hq)
            if self.seen[now]:
                continue
            self.seen[now] = 1
            self.minimunCost += min_cost
            for cost, next in self.G[now]:
                if self.seen[next]:
                    continue
                heapq.heappush(hq, (cost, next))
        return self.minimunCost
        