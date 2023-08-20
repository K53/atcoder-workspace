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
        self.sorted_longest_depth = [0] * N # トポソ後の各ノードの最長の深さ。
        return
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int):
        self.G[fromNode].append(toNode)
        self.degree[toNode] += 1
        return
        
    def topologicalSort(self):
        """
        入次数0を開始点としたBFS。
        """
        deq = deque([node for node in range(self.N) if self.degree[node] == 0]) # 入次数0のものがスタート
        # 片っ端から入次数0のものを取り出していく。取り出すとそのノードから遷移するノードの入次数をデクリメントする。
        while deq:
            cur = deq.popleft()
            self.topologicalOrder.append(cur)
            for next in self.G[cur]:
                self.degree[next] -= 1
                self.sorted_longest_depth[next] = max(self.sorted_longest_depth[next], self.sorted_longest_depth[cur] + 1)
                if self.degree[next] == 0:
                    deq.append(next)
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
            cur = heapq.heappop(hq)
            self.topologicalOrder.append(cur)
            for next in self.G[cur]:
                self.degree[next] -= 1
                self.sorted_longest_depth[next] = max(self.sorted_longest_depth[next], self.sorted_longest_depth[cur] + 1)
                if self.degree[next] == 0:
                    heapq.heappush(hq, next)
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
    
    # トポロジカルソートした結果の数列が何通りあるか -> bitDP
    # https://ferin-tech.hatenablog.com/entry/2017/01/24/184750


def bfs(G: "List[to]", start_node: int) -> list:
    INF = 10 ** 16
    q = deque()
    dist = [INF] * len(G)
    q.append(start_node)
    dist[start_node] = 0
    ans = set()
    while q:
        now = q.popleft()
        for next in G[now]:
            if dist[next] != INF:
                continue
            q.append(next)
            ans.add(next)
            dist[next] = dist[now] + 1
    return ans

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    G = [[] for _ in range(N)]
    qs = []
    for i in range(N):
        tt = list(map(int, input().split()))
        qs.append(tt)
        for num in range(tt[0]):
            G[i].append(tt[1:][num] - 1)

    ans = bfs(G, 0)

    tr = TopologicalTree(N)

    for i in range(N):
        tt = qs[i]
        for num in range(tt[0]):
            if tt[1:][num] - 1 not in ans or i not in ans:
                continue
            tr.addEdge(tt[1:][num] - 1, i)
    l = tr.topologicalSort()
    aaa = []
    for ll in l:
        if ll not in ans:
            continue
        aaa.append(ll + 1)
    print(*aaa)


if __name__ == '__main__':
    main()
