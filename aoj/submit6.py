#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C

def main():
    sys.setrecursionlimit(10 ** 9)
    class SCC():
        def __init__(self, nodesNum: int):
            self.nodesNum = nodesNum                    # 頂点数
            self.G = [[] for _ in range(self.nodesNum)] # グラフ
            self.rG = [[] for _ in range(self.nodesNum)]# 全ての辺を逆向きにしたグラフ
            self.seen = [False] * self.nodesNum         # 各ノードが訪問済みかどうかのフラグ
            self.firstOrder = []                        # ノードの行きがけ順(0-indexで採番)
            self.lastOrder = []                         # ノードの帰りがけ順(0-indexで採番)
            self.tplConnections = [-1] * self.nodesNum  # 強連結成分分解の結果(0-indexで採番。数値が若いものから順にトポロジカルソートされている)
            self.sccNum = 0                             # 強連結成分の採番用カウンタ(0-indexで採番)
        
        # 辺の追加
        def addEdge(self, fromNode: int, toNode: int):
            self.G[fromNode].append(toNode)
            self.rG[toNode].append(fromNode)

        # DFS
        def _dfs(self, now: int):
            self.firstOrder.append(now)
            self.seen[now] = True
            for next in self.G[now]:
                if self.seen[next]:
                    continue
                self._dfs(next)
            self.lastOrder.append(now)
        
        # 逆向きグラフの強連結成分チェック
        def _reverseDfs(self, now: int):
            self.seen[now] = True
            self.tplConnections[now] = self.sccNum
            for next in self.rG[now]:
                if self.seen[next]:
                    continue
                self._reverseDfs(next)
        
        # 強連結成分分解SCC
        def scc(self):
            # 帰りがけ順のナンバリングDFS
            for startNode in range(self.nodesNum):
                if self.seen[startNode]:
                    continue
                self._dfs(startNode)
            # seenをリセット
            self.seen = [False] * self.nodesNum
            # 帰りがけ順の大きい方から順に強連結成分の判定DFS
            for node in self.lastOrder[::-1]:
                if self.seen[node]:
                    continue
                self._reverseDfs(node)
                self.sccNum += 1
            return self.tplConnections
        
        # 2つのノードが強連結か。
        def same(self, a: int, b: int):
            return self.tplConnections[a] == self.tplConnections[b]

    V, E = map(int, sys.stdin.readline().split())
    d = SCC(V)
    for _ in range(E):
        s, t = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        d.addEdge(s, t)
    d.scc()
    Q = int(sys.stdin.readline())
    for _ in range(Q):
        u, v = map(lambda x: int(x) - 1, sys.stdin.readline().split())
        print(1 if d.same(u, v) else 0)
    return

if __name__ == '__main__':
    main()