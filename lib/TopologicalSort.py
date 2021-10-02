"""
1. Kahnの方法
2. Tarjanの方法
"""
# ------------------------------------------------------------------------------
#     トポロジカルソート (Kahnの方法)
# ------------------------------------------------------------------------------
# 解説
# - 1. Kahnの方法
# - キューを用いる方法。
# - 入次数が0のものから確定させて行く。
# - DAG判定 : 循環があるかどうかも判定可能(Noneを返す)。
# 
# 考察
# - 【要検証】自己ループと多重辺がある場合に入次数が正しく挙動するのか？
# 
# リンク
# - http://www.thothchildren.com/chapter/5bcc8bc051d9305189030f9f
# - https://tjkendev.github.io/procon-library/python/graph/topological_sort.html
# - https://drken1215.hatenablog.com/entry/2021/01/02/164800
# 
# 計算量
# - O(E + V) : 各ノードについて全ての頂点を1回ずつ見るため。
# 
# verify
# - https://atcoder.jp/contests/abc216/tasks/abc216_d
# ------------------------------------------------------------------------------
from collections import deque
class Tree:
    def __init__(self, N) -> None:
        self.topologicalOrder = []
        self.nodes = N
        self.seen = [0] * N
        self.G = [[] for _ in range(N)]
        self.degree = [0] * N # 各ノードの入次数
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, bothDirection: bool):
        self.G[fromNode].append(toNode)
        self.degree[toNode] += 1
        if bothDirection:
            self.G[toNode].append(fromNode)
            self.degree[fromNode] += 1
        
    
    def topologicalSort(self):
        self.topologicalOrder = [node for node in range(self.nodes) if self.degree[node] == 0] # 入次数0のものがスタート
        deq = deque(self.topologicalOrder)

        # 片っ端から入次数0のものを取り出していく。取り出すとそのノードから遷移するノードの入次数をデクリメントする。
        while deq:
            node = deq.popleft()
            for t in self.G[node]:
                self.degree[t] -= 1
                if self.degree[t] == 0:
                    deq.append(t)
                    self.topologicalOrder.append(t)
        if [i for i in range(self.nodes) if self.degree[i]]: # 最終的な入次数が0じゃないものが残る場合循環がある。
            return None
        return self.topologicalOrder

    # そのトポロジカルソートの結果が唯一のものかを返す。
    # 一般に、トポロジカルソート順 v1,v2,…,vN において、連続する2要素 vi,vi+1 の間に辺がないとき、その2要素を入れ替えることができる。
    # https://drken1215.hatenablog.com/entry/2021/01/02/164800
    def hasOtherOrder(self):
        for node in range(self.nodes - 1):
            if not self.topologicalOrder[node + 1] in self.G[self.topologicalOrder[node]]:
                return True
        else:
            return False

# usage
tr = Tree(N)
for i in range(M):
    tr.addEdge(x[i] - 1, y[i] - 1, bothDirection=False)
l = tr.topologicalSort()

# ------------------------------------------------------------------------------
#     トポロジカルソート (Tarjanの方法)
# ------------------------------------------------------------------------------
# 解説
# - 2. Tarjanの方法
# - DFSを用いる方法。
# - 帰りがけの順序で採番していき、最後に反転させる。
# 
# リンク
# -
# 
# 計算量
# - O(E + V) : DFSの計算量
# 
# Modify
# - 
# ------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10 ** 9)
class Tree:
    def __init__(self, N) -> None:
        self.topologicalOrder = []
        self.nodes = N
        self.seen = [0] * N
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, bothDirection: bool):
        self.G[fromNode].append(toNode)
        if bothDirection:
            self.G[toNode].append(fromNode)
    
    def _rec(self, now: int):
        self.seen[now] = True
        for next in self.G[now]:
            if self.seen[next]:
                continue
            self._rec(next)
        self.topologicalOrder.append(now) # DFSした末端から取って行き最後に反転。
    
    def topologicalSort(self):
        for node in range(self.nodes): # グラフが全連結じゃない可能性を考慮して全頂点からDFS。
            if self.seen[node]:
                continue
            self._rec(node)
        self.topologicalOrder = self.topologicalOrder[::-1]
        return self.topologicalOrder

    # そのトポロジカルソートの結果が唯一のものかを返す。
    # 一般に、トポロジカルソート順 v1,v2,…,vN において、連続する2要素 vi,vi+1 の間に辺がないとき、その2要素を入れ替えることができる。
    # https://drken1215.hatenablog.com/entry/2021/01/02/164800
    def hasOtherOrder(self):
        for node in range(self.nodes - 1):
            if not self.topologicalOrder[node + 1] in self.G[self.topologicalOrder[node]]:
                return True
        else:
            return False

# usage
tr = Tree(N)
for i in range(M):
    tr.addEdge(x[i] - 1, y[i] - 1, False)
l = tr.topologicalSort()
