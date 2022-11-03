#!/usr/bin/env python3
import sys

MOD = 998244353

from collections import deque
import heapq

class TopologicalTree:
    def __init__(self, N) -> None:
        self.topologicalOrder = []
        self.N = N
        self.seen = [0] * N
        self.G = [[] for _ in range(N)]
        self.degree = [0] * N # 各ノードの入次数
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int):
        self.G[fromNode].append(toNode)
        self.degree[toNode] += 1
        
    def topologicalSort(self):
        deq = deque([node for node in range(self.N) if self.degree[node] == 0]) # 入次数0のものがスタート

        # 片っ端から入次数0のものを取り出していく。取り出すとそのノードから遷移するノードの入次数をデクリメントする。
        while deq:
            node = deq.popleft()
            self.topologicalOrder.append(node)
            for t in self.G[node]:
                self.degree[t] -= 1
                if self.degree[t] == 0:
                    deq.append(t)
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
            node = heapq.heappop(hq)
            self.topologicalOrder.append(node)
            for t in self.G[node]:
                self.degree[t] -= 1
                if self.degree[t] == 0:
                    heapq.heappush(hq, t)
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
                return True
        else:
            return False
    
    # トポロジカルソートした結果の数列が何通りあるか -> bitDP
    # https://ferin-tech.hatenablog.com/entry/2017/01/24/184750


def main():
    N, Q = list(map(int, input().split()))
    queries = []
    for _ in range(Q):
        queries.append(list(map(int, input().split())))
    
    # True ------ ok | ng ---- False
    def is_ok(k: int):
        tr = TopologicalTree(N)
        for a, b in queries[:k]:
            tr.addEdge(a - 1, b - 1)
        l = tr.topologicalSort()
        # print("#", l)
        return l != None    # 条件式

    def binSearch(ok: int, ng: int):
        # print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            # print("target > ", mid)
            result = is_ok(mid)
            # print(result)
            if result:
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            # print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ng    # 関数呼び出し時の引数のngは絶対評価されないのでngに書く値が答えになりうるならその数マイナス1を指定する。

    ans = binSearch(0, Q)
    print(ans if ans < Q else -1)
    return

if __name__ == '__main__':
    main()
