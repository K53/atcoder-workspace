#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str

from collections import deque
class Tree:
    def __init__(self, N) -> None:
        self.topologicalOrder = []
        self.nodes = N
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
        self.topologicalOrder = [node for node in range(self.nodes) if self.degree[node] == 0] # 入次数0のものがスタート
        deq = deque(self.topologicalOrder)

        # 片っ端から入次数0のものを取り出していく。取り出すとそのノードから遷移するノードの入次数をデクリメントする。
        while deq:
            node = deq.popleft()
            for t in self.G[node]:
                self.degree[t] -= 1
                if self.degree[t] == 0:
                    deq.append(t)
                    self.topologicalOrder.append(t)
        if [i for i in range(self.nodes) if self.degree[i]]: # 最終的な入次数が0じゃないものが残る場合循環がある。
            return None
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




def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    tr = Tree(N)
    for _ in range(M):
        k = int(input())
        A = list(map(int, input().split()))
        for i in range(k - 1):
            tr.addEdge(A[i] - 1, A[i + 1] - 1, bothDirection=False)
    l = tr.topologicalSort()
    if l == None:
        print(NO)
    else:
        print(YES)
    # print(l)


if __name__ == '__main__':
    main()
