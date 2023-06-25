INF = 10 ** 18

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
        # print("Really directed Graph?")
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


def build(G: "list[list[int]]", start: int, sum: int):
    N = len(G)
    rev = [-1] * N # parents
    weight = [INF] * N
    for i in range(N):
        for to, cost in G[i]:
            if cost < weight[to]:
                weight[to] = cost
                rev[to] = i
    # print(rev)
    scc = SCC(N)
    for i in range(N):
        if start == i:
            continue
        if rev[i] == -1:
            return INF
        scc.addEdge(rev[i], i)
        sum += weight[i]
    
    associates = scc.build()
    # print(associates, sum)
    # print(scc.sccNum, "$")
    if scc.sccNum == N:
        return sum
    newG = [[] for _ in range(scc.sccNum)]
    for i in range(N):
        for to, cost in G[i]:
            if scc.same(i, to):
                continue
            newG[associates[i]].append((associates[to], cost - weight[to]))
    # print(newG)
    return build(newG, associates[start], sum)

N, M, root = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    s, t, w = map(int, input().split())
    G[s].append((t, w))

ans = build(G, root, 0)
# if ans >= INF:
#     print(-1)
# else:
print(ans)


