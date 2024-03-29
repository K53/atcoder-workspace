#!/usr/bin/env python3
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

#usage
# # 木の構築
# d = SCC(6)
# A = [1, 5, 3, 5, 4, 0, 4]
# B = [4, 2, 0, 5, 1, 3, 2]
# for aa, bb in zip(A, B):
#     d.addEdge(fromNode=aa, toNode=bb)
# # ビルド
# associates = d.build()
# print(associates) # SCC後の対応表(indexがノード番号。値が0-indexで採番されたSCCのグループの順番。値が若いものから順にトポロジカルソートされている)
# '-> [3, 1, 2, 3, 1, 0]'
# # 全SCC取得。トポロジカル順序で出力。
# print(d.getAllSccGroups())
# '-> [[5], [1, 4], [2], [0, 3]]'
# # SCCは不要で、強連結成分分解した後のトポロジカルソートされたリストが欲しいなら以下の方が早い。
# print(d.topologicalSortedList)
# '-> [5, 1, 4, 2, 0, 3]'

def solve(N: int, X: "List[int]", C: "List[int]"):
    d = SCC(N)
    for i in range(N):
        d.addEdge(fromNode=i, toNode=(X[i] - 1))
    associates = d.build()
    ans = 0
    # print(associates)
    # print(d.getAllSccGroups())
    for ll in d.getAllSccGroups():
        if len(ll) == 1:
            continue
        count = 10 ** 10
        for lll in ll:
            count = min(count, C[lll])
        ans += count
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, C)

if __name__ == '__main__':
    main()
