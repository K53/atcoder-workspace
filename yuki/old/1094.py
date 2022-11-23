#!/usr/bin/env python3
import sys

class LcaDoubling:
    # 木であれば任意の点を根と見做せる。
    def __init__(self, N, root=0):
        self.N = N
        self.root = root
        self.G = [[] for _ in range(N)]
        self.depths = [-1] * N
        self.distances = [-1] * N
        self.ancestors = []
        return
    
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((cost, toNode))
        # print("Really directed Graph?")
        return
    
    def build(self):
        prevAncestors = self._dfs()
        self.ancestors.append(prevAncestors)
        d = 1
        max_depth = max(self.depths)
        while d < max_depth:
            nextAncestors = [prevAncestors[p] for p in prevAncestors]
            self.ancestors.append(nextAncestors)
            d <<= 1
            prevAncestors = nextAncestors
        return

    def _dfs(self):
        q = [(self.root, -1, 0, 0)]
        directAncestors = [-1] * (self.N + 1)  # 頂点数より1個長くし、存在しないことを-1で表す。末尾(-1)要素は常に-1
        while q:
            now, parent, dep, dist = q.pop()
            directAncestors[now] = parent
            self.depths[now] = dep
            self.distances[now] = dist
            for cost, next in self.G[now]:
                if next != parent:
                    q.append((next, now, dep + 1, dist + cost))
        return directAncestors
 
    def getLca(self, nodeA: int, nodeB: int):
        depthA, depthB = self.depths[nodeA], self.depths[nodeB]
        if depthA > depthB:
            nodeA, nodeB = nodeB, nodeA
            depthA, depthB = depthB, depthA
        
        # 2ノードを同じ深さまで揃える。
        tu = nodeA
        tv = self.upstream(nodeB, depthB - depthA)

        # 遡上させて行き2つが衝突する位置が共通祖先。
        if nodeA == tv:
            return nodeA
        for k in range(depthA.bit_length() - 1, -1, -1):
            mu = self.ancestors[k][tu]
            mv = self.ancestors[k][tv]
            if mu != mv:
                tu = mu
                tv = mv
        lca = self.ancestors[0][tu]
        assert lca == self.ancestors[0][tv]
        return lca
 
    # 2つのノードの間の距離を返す。
    def getDistance(self, nodeA, nodeB):
        lca = self.getLca(nodeA, nodeB)
        return self.distances[nodeA] + self.distances[nodeB] - 2 * self.distances[lca]

    # targetNodeが2つのノード間のパス上に存在するかを返す。
    def isOnPath(self, nodeA: int, nodeB: int, evalNode: int):
        return self.getDistance(nodeA, nodeB) == self.getDistance(nodeA, evalNode) + self.getDistance(evalNode, nodeB) 

    # ノードvからk個遡上したノードを返す。
    def upstream(self, v, k):
        i = 0
        while k:
            if k & 1:
                v = self.ancestors[i][v]
            k >>= 1
            i += 1
        return v

def main():
    N = int(input())
    ld = LcaDoubling(N)
    for _ in range(N - 1):
        a, b, c = map(int, input().split())
        ld.addEdge(fromNode=a - 1, toNode=b - 1, cost=c)
        ld.addEdge(fromNode=b - 1, toNode=a - 1, cost=c)
    ld.build()
    Q = int(input())
    for _ in range(Q):
        s, t = map(int, input().split())
        print(ld.getDistance(nodeA=s - 1, nodeB=t - 1))

if __name__ == '__main__':
    main()