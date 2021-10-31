#!/usr/bin/env python3
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
    def addEdge(self, fromNode: int, toNode: int, bothDirection: bool):
        self.G[fromNode].append(toNode)
        self.degree[toNode] += 1
        if bothDirection:
            self.G[toNode].append(fromNode)
            self.degree[fromNode] += 1
        
    
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
                return False
        else:
            return True

def main():
    n = int(input())
    m = int(input())
    tt = TopologicalTree(n)
    for _ in range(m):
        i, j = map(int, input().split())
        tt.addEdge(i - 1, j - 1, bothDirection=False)
    l = tt.topologicalSort()
    ans = map(lambda i: i + 1, l)
    print(*ans, sep="\n")
    print(0 if tt.isUniqueOrder() else 1)

if __name__ == '__main__':
    main()
