# ------------------------------------------------------------------------------
#     ベルマンフォード法 (BellmanFord)
# ------------------------------------------------------------------------------
# 解説
# - 全ての辺について、その辺を通ることで移動先のノードの最小コストが更新されるならする。この際、移動元のコストは幾つであっても信用する。
# - この処理を頂点数N回だけ実施すると必ず全てのノードで最小コストになっている。
# - さらにN + 1回目を実施した時に更新が発生した場合、それはどこかに閉路があり、無限にコストを下げられる状態にあると判断できる。
# - 以降、その辺から到達可能な辺は全て不定(-INF)として潰すので再度N回回す。 
# 
# Note
#   始点から到達不可能な負閉路の有無： ×　(ベルマンフォード法では発見されない)
#       [S]      [ ]
#        |      /   \
#       [G]  [ ] --- [ ]
#   始点から到達可能だが終点に影響ない負閉路の有無： ○ (出力のリストに-INFが含まれるかどうか)
#       [S] ------ [ ]
#        |        /   \
#       [G] -> [ ] --- [ ] # 一方通行なので影響無
#   始点から到達可能で終点に到達する負閉路の有無：　○ (出力のリストの終点へのコストが-INFかどうか)
#       [S] ------ [ ]
#        |        /   \
#       [G] -- [ ] --- [ ]
#
# Link
# - https://qiita.com/Kept1994/items/0b185def44fca1aa64ed
# 
# Order
#   O(2V * E)
#   ← ダイクストラ O(V + ElogE) に比べて低速なので負の辺がないならダイクストラを使用するべき。 
#
# verify
# - https://atcoder.jp/contests/abc137/tasks/abc137_e (グラフ)
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#  グラフ (verified)
# ------------------------------------------------------------------------------
import sys
INF = 10 ** 16

class BellmanFord():
    def __init__(self, N: int) -> None:
        self.N = N 
        self.E: "list[tuple(int, int, int)]" = [] # ダイクストラ等と異なりベルマンフォード法では辺に着目する
        return
    
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.E.append((fromNode, toNode, cost))
        print("Really directed Graph?")
        return
    
    def build(self, startNode: int):
        dist = [INF] * self.N
        dist[startNode] = 0
        # 少なくとも頂点数N回だけ全部の辺について最短手数を更新すれば最短経路がもとまる。 O(V * E)
        # N + 1回目に更新が発生するということは閉路があるということなので、そこから到達可能な辺は全て影響を受けることから=INFで潰す。 O(V * E)
        for i in range(self.N * 2):
            for fromNode, toNode, cost in self.E:
                if dist[fromNode] != INF and dist[toNode] > dist[fromNode] + cost:
                    if i >= self.N - 1:
                        dist[toNode] = -INF
                    else:
                        dist[toNode] = dist[fromNode] + cost
        return dist

# Usage
N = 3
A = [1,2,1]
B = [2,3,3]
C = [20,30,45]

bf = BellmanFord(N)
for aa, bb, cc in zip(A, B, C):
    bf.addEdge(aa - 1, bb - 1, C) 

dist = bf.build(startNode=0)

if dist[-1] == -INF: print("不定") # 始点から到達可能で終点に到達する負閉路である。
for i in dist:
    if i < 0: print(dist[-1], "負閉路はあり") # 始点から到達可能だが終点に影響ない負閉路である。