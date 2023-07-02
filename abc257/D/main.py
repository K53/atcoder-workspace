#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
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

class MinimumCostArborescence():
    def __init__(self, N: int) -> None:
        # self.minimumG = [[] for _ in range(N)] # 全域最小木自体が欲しい場合にはこれを有効にする。　todo
        self.G = [[] for _ in range(N)]
        return
    
    def addEdge(self, a: int, b: int, cost: int):
        self.G[a].append((b, cost))
        return

    def _build(self, G: "list[list[int]]", start: int, ans: int):
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
            ans = max(ans, min_cost[cur])
        
        # 強連結成分分解後の対応表
        associates = scc.build() # associates[i] = ノードiが属する連結成分の番号(0-indexedで採番されている)

        # 分解後の連結成分数sccNum = 分解前のノード数N であればこれ以上は強連結成分はないとわかるので縮約操作を終了する。
        if scc.sccNum == N:
            return ans
        
        cc = [INF] * scc.sccNum
        for cur in range(N): # 全ての辺を捜査
            for to, cost in G[cur]:
                if scc.same(cur, to): # 閉路に属している辺なら
                    continue
                cc[associates[cur]] = max(cc[associates[cur]], cost)

        # 同一の連結成分に属するノードを縮約し、連結成分の番号をノード番号として新たなグラフを構築する。
        newG = [[] for _ in range(scc.sccNum)]
        for i in range(N): # 全ての辺を捜査
            for to, cost in G[i]:
                if scc.same(i, to): # 閉路に属している辺なら
                    continue
                newG[associates[i]].append((associates[to], min(cc[associates[i]], cost)))

        return self._build(newG, associates[start], ans)

    def build(self, root):
        return self._build(self.G, root, 0)

def solve(N: int, x: "List[int]", y: "List[int]", P: "List[int]"):
    mca = MinimumCostArborescence(N)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            mca.addEdge(i, j, (abs(x[i] - x[j]) + abs(y[i] - y[j]) + P[i] - 1) // P[i])
    ans = INF
    for i in range(N):
        ans = min(ans, mca.build(i))
    print(ans)



# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        P[i] = int(next(tokens))
    solve(N, x, y, P)

if __name__ == '__main__':
    main()
