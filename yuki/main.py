#!/usr/bin/env python3
import sys
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.group_num = n
        self.parents = [-1] * n

    """ 要素xの値を取得。"""
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    """ 2つの要素の併合。"""
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.group_num -= 1
        return

    """ 要素xの属する集合の要素数を取得。"""
    def size(self, x):
        return -self.parents[self.find(x)]

    """ 2つの要素が同一の集合に属するか。"""
    def same(self, x, y):
        return self.find(x) == self.find(y)

    """ 要素xと同一の集合の要素を全取得。
    計算量 : O(N)
    """
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    """ 各集合の根を全取得。
    計算量 : O(N)
    """
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    """ 集合の個数を取得。 v2
    計算量 : O(1)
    """
    def group_count_v2(self):
        return self.group_num

    """ 集合の個数を取得。 v1
    計算量 : O(N)
    """
    def group_count_v1(self):
        return len(self.roots())

    """ 全集合の要素一覧を取得。
    計算量 : O(N)
    """
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
    
sys.setrecursionlimit(10 ** 9)
class SCC():
    def __init__(self, N: int):
        self.N = N                                              # 頂点数
        self.G = [[] for _ in range(self.N)]                    # 与えられたグラフ
        self.rG = [[] for _ in range(self.N)]                   # 全ての辺を逆向きにしたグラフ
        self.seen = [False] * self.N                            # 各ノードが訪問済みかどうかのフラグ
        self.lastOrder = []                                     # ノードの帰りがけ順(0-indexで採番)
        self.associationNodeNumWithSccGroupNum = [-1] * self.N  # SCC後の対応表(indexがノード番号。値が0-indexで採番されたSCCのグループの順番。値が若いものから順にトポロジカルソートされている)
        self.topologicalSortedList = []                         # SCC後のトポロジカルソート済みリスト
        self.sccNum = 0                                         # SCCの個数 兼 強連結成分の採番用カウンタ(0-indexで採番)
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int):
        # グラフ構築
        self.G[fromNode].append(toNode)
        # 逆向きグラフを別途構築
        self.rG[toNode].append(fromNode)

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
        self.topologicalSortedList.append(now)
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



def main():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        uf.union(A - 1, B - 1)
    dags = uf.all_group_members()
    print(dags)
    print(G)
    ans = []
    for d in dags.values():
        compressed = {}
        compressed_to_row = []
        for index, val in enumerate(sorted(list(set(d)))):
            compressed[val] = index
            compressed_to_row.append(val)
        # print(compressed)
        sc = SCC(len(d))
        for i in d:
            for j in G[i]:
                sc.addEdge(compressed[i], compressed[j])
        sc.build()
        for i in range(len(d) - 1):
            ans.append(f"{compressed_to_row[sc.topologicalSortedList[i]] + 1} {compressed_to_row[sc.topologicalSortedList[i + 1]] + 1}")
    print(len(ans))
    print(*ans, sep="\n")
    return

if __name__ == '__main__':
    main()