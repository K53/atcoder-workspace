#!/usr/bin/env python3
import sys
from collections import defaultdict
import heapq
INF = 10 ** 16
# グラフ + 座標圧縮 の問題の場合、開始点と終了点を圧縮後の座標の集合に加え忘れないこと。
class Dijkstra():
    def __init__(self, N: int) -> None:
        self.N = N 
        self.G = [[] for _ in range(N)]
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((cost, toNode))
        return

    # "toノードに到達するための辺の番号"を同時に持たせることで経路復元時にedge_numを使用できる。
    # def addEdge(self, fromNode: int, toNode: int, cost: int, edge_num: int):
    #     self.G[fromNode].append((cost, toNode, edge_num))
    #     return
    
    def build(self, startNode: int):
        """
        多始点ダイクストラの場合、初期化するdistとヒープを各スタートノード分やってbuildすればいい。
        これは単一の超頂点をスタートとして与えられた多始点それぞれにコスト0の辺が伸びていたと解釈すれば成立すると分かる。
        """
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [INF] * self.N
        # prev = [-1] * self.N # 経路復元する場合は移動時に直前の頂点や辺を記録して遷移していく。
        heapq.heappush(hq, (0, startNode))
        dist[startNode] = 0
        # dijkstra
        while hq:
            min_cost, now = heapq.heappop(hq)
            if min_cost > dist[now]:
                continue
            for cost, next in self.G[now]:
                if dist[next] > dist[now] + cost:
                    dist[next] = dist[now] + cost
                    # prev[next] = now # 頂点nextに至る直前の頂点(now)または辺(edge_num)を更新。
                    heapq.heappush(hq, (dist[next], next))
        return dist



class UnionFind():
    def __init__(self, n):
        self.n = n
        self.group_num = n
        self.parents = [-1] * n # サイズ

    def find(self, x):
        """ 要素xの親を取得。"""
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x]) # 経路圧縮
            return self.parents[x]

    def union(self, x, y):
        """ 2つの要素の併合。"""
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

    def size(self, x):
        """ 要素xの属する集合の要素数を取得。"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """ 2つの要素が同一の集合に属するか。"""
        return self.find(x) == self.find(y)

    def members(self, x):
        """ 要素xと同一の集合の要素を全取得。
        計算量 : O(N)
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """ 各集合の根を全取得。
        計算量 : O(N)
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count_v2(self):
        """ 集合の個数を取得。 v2
        計算量 : O(1)
        """
        return self.group_num

    def group_count_v1(self):
        """ 集合の個数を取得。 v1
        計算量 : O(N)
        """
        return len(self.roots())

    def all_group_members(self) -> dict:
        """ 全集合の要素一覧を取得。
        key : 根 (int)
        value : 要素ノード (list[int])
        計算量 : O(N)
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

class Kruskal():
    def __init__(self, N: int) -> None:
        self.minimumG = [[] for _ in range(N)] # 全域最小木自体が欲しい場合にはこれを有効にする。
        self.edges = []
        self.uf =  UnionFind(N)
        self.minimunCost = 0 # 最小全域木を構成する全体のコストの総和の最小。
        return
    
    def addEdge(self, a: int, b: int, cost: int):
        self.edges.append((cost, a, b))
        return
    
    def build(self):
        for cost, a, b in sorted(self.edges):
            if self.uf.same(a, b):
                continue
            self.minimunCost += cost
            self.uf.union(a, b)
            # --- 全域最小木自体を構築 ---
            self.minimumG[a].append(b)
            self.minimumG[b].append(a)
        return self.minimunCost

def solve(N: int, M: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    G = [[] for _ in range(N)]
    for aa, bb, cc in zip(A, B, C):
        G[aa - 1].append((bb - 1, cc))
        G[bb - 1].append((aa - 1, cc))
    
    sec = set()
    def dfs(cur, dist):
        move = 0
        for next, dd in G[cur]:
            if dist[next] != -INF:
                continue
            dist[next] = dist[cur] + dd
            move += 1
            dfs(next, dist)
            dist[next] = -INF
        if move == 0:
            mm = -INF
            mp = -1
            for i in range(N):
                if dist[i] > mm:
                    mm = dist[i]
                    mp = i
            sec.add(mp)

    ans = -INF
    def dfs2(cur, dist):
        nonlocal ans
        move = 0
        for next, dd in G[cur]:
            if dist[next] != -INF:
                continue
            dist[next] = dist[cur] + dd
            move += 1
            dfs2(next, dist)
            dist[next] = -INF
        if move == 0:
            ans = max(ans, max(dist))

    for st in range(N):
        dist = [-INF] * N
        dist[st] = 0
        dfs(st, dist)

    for st in sec:
        dist = [-INF] * N
        dist[st] = 0
        dfs2(st, dist)
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
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, A, B, C)

if __name__ == '__main__':
    main()
