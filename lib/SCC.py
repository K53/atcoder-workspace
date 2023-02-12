# ------------------------------------------------------------------------------
#     強連結成分分解 SCC(Strongly Connected Component)
# ------------------------------------------------------------------------------
# 解説
# - 強連結成分とは、有向グラフにおいて、互いに行き来が可能な頂点の集合。
# - 有向グラフをDFSし、帰りがけ順でナンバリングする。
# - 向きを逆にしたグラフにおいて、帰りがけ順の大きい番号からDFSし、通過する箇所はSCCとわかる。
# - (帰りがけ順の大きい番号は最後に描かれるので、常にグラフの部分集合の根にあたるはず。
# - 仮にその頂点がSCCでないなら反転したグラフでは末端側となり、行き場はないはず。
# - その根から移動できる箇所があるということはそれはSCCとなっており、その移動可能な範囲を網羅する。)
# 
# リンク
# - https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html
# 
# 計算量
# - O(V + E) : 要するに2回のDFSなので。
# 
# verify
# - https://atcoder.jp/contests/practice2/tasks/practice2_g?lang=ja
# - https://atcoder.jp/contests/typical90/tasks/typical90_u
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C&lang=jp
# ------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10 ** 9)
class SCC():
    def __init__(self, N: int):
        self.N = N                                              # 頂点数
        self.G = [[] for _ in range(self.N)]                    # 与えられたグラフ
        self.rG = [[] for _ in range(self.N)]                   # 全ての辺を逆向きにしたグラフ
        self.seen = [False] * self.N                            # 各ノードが訪問済みかどうかのフラグ
        self.lastOrder = []                                     # ノードの帰りがけ順(0-indexで採番)
        self.associationNodeNumWithSccGroupNum = [-1] * self.N  # SCC後の対応表(indexがノード番号。値が0-indexで採番されたSCCのグループの順番。値が若いものから順にトポロジカルソートされている)
        # self.topologicalSortedList = []                         # SCC後のトポロジカルソート済みリスト
        self.sccNum = 0                                         # SCCの個数 兼 強連結成分の採番用カウンタ(0-indexで採番)
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int):
        # グラフ構築
        self.G[fromNode].append(toNode)
        # 逆向きグラフを別途構築
        self.rG[toNode].append(fromNode)
        print("Really directed Graph?")
        return

    # DFS
    def _dfs(self, now: int):
        self.seen[now] = True
        for next in self.G[now]:
            if self.seen[next]:
                continue
            self._dfs(next)
        self.lastOrder.append(now)
    
    # 逆向きグラフの強連結成分チェック
    def _reverseDfs(self, now: int):
        self.seen[now] = True
        self.associationNodeNumWithSccGroupNum[now] = self.sccNum
        # self.topologicalSortedList.append(now)
        for next in self.rG[now]:
            if self.seen[next]:
                continue
            self._reverseDfs(next)
    
    # 強連結成分分解SCC
    def build(self):
        # 帰りがけ順のナンバリングDFS
        for startNode in range(self.N):
            if self.seen[startNode]:
                continue
            self._dfs(startNode)
        # seenをリセット
        self.seen = [False] * self.N
        # 帰りがけ順の大きい方から順に強連結成分の判定DFS
        for node in self.lastOrder[::-1]:
            if self.seen[node]:
                continue
            self._reverseDfs(node)
            self.sccNum += 1
        return self.associationNodeNumWithSccGroupNum
    
    # 2つのノードが強連結か。
    def same(self, a: int, b: int):
        return self.associationNodeNumWithSccGroupNum[a] == self.associationNodeNumWithSccGroupNum[b]

    # 強連結成分SCCを全取得。
    def getAllSccGroups(self):
        res = [[] for _ in range(self.sccNum)]
        for nodeNum, sccGroupNum in enumerate(self.associationNodeNumWithSccGroupNum):
            res[sccGroupNum].append(nodeNum)
        return res

#usage
# 木の構築
d = SCC(6)
A = [1, 5, 3, 5, 4, 0, 4]
B = [4, 2, 0, 5, 1, 3, 2]
# イメージ
#  (1)
#  ↓ ↑
#  (4)
#   ↓
#  (2) ← (5) ⇆ (5) # 自己ループ
#
#  (3) ⇆ (0)
for aa, bb in zip(A, B):
    d.addEdge(fromNode=aa, toNode=bb)
# ビルド
associates = d.build()
print(associates) # SCC後の対応表(indexがノード番号。値が0-indexで採番されたSCCのグループの順番。値が若いものから順にトポロジカルソートされている)
'-> [3, 1, 2, 3, 1, 0]'
# 全SCC取得。トポロジカル順序で出力。
print(d.getAllSccGroups())
'-> [[5], [1, 4], [2], [0, 3]]'
# SCCは不要で、強連結成分分解した後のトポロジカルソートされたリストが欲しいなら以下の方が早い。
# print(d.topologicalSortedList)
'-> [5, 1, 4, 2, 0, 3]'

print(d.lastOrder)