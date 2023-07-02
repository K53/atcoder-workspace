# ------------------------------------------------------------------------------
#     最小有向全域木 (Minimum Cost Arborescence)
# ------------------------------------------------------------------------------
# tag: 最小全域有向木 有向最小全域木
#
# 解説
# 
# リンク
# - https://ti2236.hatenablog.com/entry/2012/12/07/175841
# - https://37zigen.com/minimum-arborescence/
# - https://ei1333.github.io/algorithm/chu-liu-edmond.html (実装)
# - https://tjkendev.github.io/procon-library/python/graph/chu-liu-edmonds.html (実装 : SCCしないver)
# 
# 計算量
# - O(VE)
#
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_B&lang=ja
# ------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
from SCC import SCC

class MinimumCostArborescence():
    def __init__(self, N: int) -> None:
        # self.minimumG = [[] for _ in range(N)] # 全域最小木自体が欲しい場合にはこれを有効にする。　todo
        self.G = [[] for _ in range(N)]
        return
    
    def addEdge(self, a: int, b: int, cost: int):
        self.G[a].append((b, cost))
        return

    def _build(self, G: "list[list[int]]", start: int, sum: int):
        N = len(G) # グラフのノード数
        
        # 全てのノードに対して親とそのノードへ流入する最小コストをメモ
        parents = [-1] * N          # parents[i] := ノードiの親ノード番号
        min_cost = [INF] * N        # min_cost[i] := ノードiへ流入する辺の中の最小コスト
        for i in range(N):
            for to, cost in G[i]:
                if cost < min_cost[to]:
                    min_cost[to] = cost
                    parents[to] = i
        
        # 各ノードに流入する最小コストのみaddEdgeした木で強連結成分分解
        scc = SCC(N)
        for cur in range(N):
            if start == cur: # start(根)に該当するなら流入は考慮しない。
                continue
            if parents[cur] == -1: # 根以外で親がないノードがある木 = 到達不可のため解無し
                return INF
            scc.addEdge(parents[cur], cur)
            sum += min_cost[cur]
        print(scc.G)
        
        # 強連結成分分解後の対応表
        associates = scc.build() # associates[i] = ノードiが属する連結成分の番号(0-indexedで採番されている)
        print(associates)
        # 分解後の連結成分数sccNum = 分解前のノード数N であればこれ以上は強連結成分はないとわかるので縮約操作を終了する。
        if scc.sccNum == N:
            return sum
        
        # 同一の連結成分に属するノードを縮約し、連結成分の番号をノード番号として新たなグラフを構築する。
        newG = [[] for _ in range(scc.sccNum)]
        for cur in range(N): # 全ての辺を捜査
            for to, cost in G[cur]:
                if scc.same(cur, to): # 閉路に属している辺なら
                    continue
                newG[associates[cur]].append((associates[to], cost - min_cost[to]))

        return self._build(newG, associates[start], sum)

    def build(self, root):
        return self._build(self.G, root, 0)

N = 4
edges = [
    (0, 1, 3),
    (0, 2, 2),
    (2, 0, 1),
    (2, 3, 1),
    (3, 0, 1),
    (3, 1, 5)
]

mca = MinimumCostArborescence(N)
for s, t, c in edges:
    mca.addEdge(s, t, c)
ans = mca.build(root=3)
print(ans)

# 絵にすると以下
#
# ■ _build()コール 1週目
#
#     [1] ← 5 ← [3]Root # 根への流入は無視されるので 0→2→3は閉路ではない : 縮約しない
#      ↑      ↙︎  ↑
#      3    1    1
#      ↑ ↙︎       ↑
#     [0] → 2 → [2]  #
#      ↑         |   # 0⇄2 ここは閉路なので縮約対象になる
#      -----1----    #
#
# - そのノードに流入する最小コストはどの辺を通っても確実に発生するコストなのでsumに加算しておき、
# - 残りの変からその分を減算してグラフを構築する。
#
# sum : 6 (= 3 + 1 + 2 : 根は除くため)
# 
# ■ _build()コール 2週目
# 
#     [2] ← 2 ← [0]Root # 根への流入は無視されるので 0→1は閉路ではない : 縮約しない
#      ↑      ↙︎  ↑
#      0    0    0
#      ↑ ↙︎       ↑
#     [     1     ]
#
# - これ以上縮約されないのでsum (6)を返却する。
