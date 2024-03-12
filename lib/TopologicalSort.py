"""
1. Kahnの方法 ※ DAG判定可能 / 辞書順最小取得
2. Tarjanの方法
"""
# ------------------------------------------------------------------------------
#     トポロジカルソート (Kahnの方法)
# ------------------------------------------------------------------------------
# → DAG判定可能 (DFSのTarjanの方法でもできるはずだがライブラリ未整備)、SCCでもDAG判定は可能。
# 
# 解説
# - 1. Kahnの方法
# - キューを用いる方法。入次数が0のものから確定させて行く。
# - <処理>
# - 1. 入次数0の頂点をキューから取り出す。
# - 2. その頂点とその頂点から出る辺をグラフから削除する。
# - 3. 2の結果入次数が0になったものをキューに追加。
# - 4. 1-3の繰り返し。循環があった場合(入次数が全て0にならなかった場合) = DAG判定 (Noneを返す)。
# 
# 考察
# - 【要検証】自己ループと多重辺がある場合に入次数が正しく挙動するのか？
# 
# リンク
# - http://www.thothchildren.com/chapter/5bcc8bc051d9305189030f9f
# - https://tjkendev.github.io/procon-library/python/graph/topological_sort.html
# - https://drken1215.hatenablog.com/entry/2021/01/02/164800
# - https://o-treetree.hatenablog.com/entry/2020/05/20/222333
# 
# 計算量
# - O(E + V) : 各ノードについて全ての頂点を1回ずつ見るため。
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B&lang=ja (シンプルなverify)
# - https://atcoder.jp/contests/abc223/tasks/abc223_d (辞書順最小を求められる問題)
# - https://atcoder.jp/contests/tenka1-2016-quala/tasks/tenka1_2016_qualA_c (辞書順最小を求める問題 文字列)
# - https://atcoder.jp/contests/joi2007ho/tasks/joi2007ho_d (単一のトポロジカル順序かの判定)
# - https://atcoder.jp/contests/abc216/tasks/abc216_d 
# - https://atcoder.jp/contests/past202107-open/tasks/past202107_j (DAG判定)
# - https://atcoder.jp/contests/abc139/tasks/abc139_e (トポソ後の深さ)
# ------------------------------------------------------------------------------
from collections import deque
import heapq

class TopologicalTree:
    def __init__(self, N) -> None:
        self.topologicalOrder = []
        self.N = N
        self.seen = [0] * N
        self.G = [[] for _ in range(N)]
        self.degree = [0] * N # 各ノードの入次数
        self.sorted_longest_depth = [0] * N # トポソ後の各ノードの最長の深さ。
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int):
        self.G[fromNode].append(toNode)
        self.degree[toNode] += 1
        print("Really directed Graph?")
        return
        
    def topologicalSort(self):
        """
        入次数0を開始点としたBFS。
        """
        deq = deque([node for node in range(self.N) if self.degree[node] == 0]) # 入次数0のものがスタート
        # 片っ端から入次数0のものを取り出していく。取り出すとそのノードから遷移するノードの入次数をデクリメントする。
        while deq:
            cur = deq.popleft()
            self.topologicalOrder.append(cur)
            for next in self.G[cur]:
                self.degree[next] -= 1
                self.sorted_longest_depth[next] = max(self.sorted_longest_depth[next], self.sorted_longest_depth[cur] + 1)
                if self.degree[next] == 0:
                    deq.append(next)
        if [i for i in range(self.N) if self.degree[i]]: # 最終的な入次数が0じゃないものが残る場合循環がある。
            return None
        return self.topologicalOrder

    def topologicalSort_heapq(self):
        """
        辞書順最小のトポロジカル順序を必要とする場合。
        queueではなくheapqを使うため、入次数0のものの中で辞書順最小のnodeが選ばれる。
        """
        hq = [node for node in range(self.N) if self.degree[node] == 0] # 入次数0のものがスタート
        heapq.heapify(hq)
        # 片っ端から入次数0のものを取り出していく。取り出すとそのノードから遷移するノードの入次数をデクリメントする。
        while hq:
            cur = heapq.heappop(hq)
            self.topologicalOrder.append(cur)
            for next in self.G[cur]:
                self.degree[next] -= 1
                self.sorted_longest_depth[next] = max(self.sorted_longest_depth[next], self.sorted_longest_depth[cur] + 1)
                if self.degree[next] == 0:
                    heapq.heappush(hq, next)
        if [i for i in range(self.N) if self.degree[i]]: # 最終的な入次数が0じゃないものが残る場合循環がある。
            return None
        return self.topologicalOrder

    def isUniqueOrder(self):
        """
        トポロジカル順序が一意に定まるかを返す。
        一般に、トポロジカルソート順 v1,v2,…,vN において、連続する2要素 vi,vi+1 の間に辺がないとき、その2要素を入れ替えることができることを利用。
        https://drken1215.hatenablog.com/entry/2021/01/02/164800
        """
        for node in range(self.N - 1):
            if not self.topologicalOrder[node + 1] in self.G[self.topologicalOrder[node]]:
                return False
        else:
            return True
    
    # トポロジカルソートした結果の数列が何通りあるか -> bitDP
    # https://ferin-tech.hatenablog.com/entry/2017/01/24/184750

# usage
N, M = 4, 3
x = [2, 3, 2]
y = [1, 4, 4]

tr = TopologicalTree(N)
for i in range(M):
    tr.addEdge(x[i] - 1, y[i] - 1)
l = tr.topologicalSort()
print(l)
"-> [1, 2, 0, 3]"
l = tr.topologicalSort_heapq()
print(l)
"-> [1, 0, 2, 3] # heapqによる辞書順最小の場合。"
# -> None # DAGでない場合 (= DAG判定)。

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
class TopologicalTree:
    def __init__(self, N) -> None:
        self.topologicalOrder = []
        self.nodes = N
        self.seen = [0] * N
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int):
        self.G[fromNode].append(toNode)
        print("Really directed Graph?")
        return

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
    
    # トポロジカルソートした結果の数列が何通りあるか -> bitDP
    # https://ferin-tech.hatenablog.com/entry/2017/01/24/184750

# usage
tr = TopologicalTree(N)
for i in range(M):
    tr.addEdge(x[i] - 1, y[i] - 1)
l = tr.topologicalSort()
