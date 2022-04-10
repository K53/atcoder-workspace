#!/usr/bin/env python3
import sys
from collections import deque
import heapq
YES = "Yes"  # type: str
NO = "No"  # type: str
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
    

def solve(N: int, M: int, u: "List[int]", v: "List[int]"):
    tr = TopologicalTree(N)
    for i in range(M):
        tr.addEdge(u[i] - 1, v[i] - 1)
    l = tr.topologicalSort()
    print(YES if l == None else NO)




# Generated by 2.11.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, M, u, v)

if __name__ == '__main__':
    main()
