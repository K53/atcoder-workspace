#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

class LcaDoubling:
    # 木であれば任意の点を根と見做せる。
    def __init__(self, N, root=0):
        self.N = N
        self.root = root
        self.G = [[] for _ in range(N)]
        self.depths = [-1] * N
        self.distances = [-1] * N
        self.ancestors = [] # ダブリングによって求めた祖先の配列の配列 i番目の配列は過去ノードの2^i個祖先のノードを格納する。
        return
    
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((cost, toNode))
        return
    
    def build(self):
        """
        O(NlogN)
        """
        prevAncestors = self._bfs()
        self.ancestors.append(prevAncestors)
        d = 1
        max_depth = max(self.depths)
        while d < max_depth:
            nextAncestors = [prevAncestors[p] for p in prevAncestors]
            self.ancestors.append(nextAncestors)
            d <<= 1
            prevAncestors = nextAncestors
        return

    def _bfs(self):
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
        """
        O(logN)
        """
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
        """
        O(logN)
        """
        lca = self.getLca(nodeA, nodeB)
        return self.distances[nodeA] + self.distances[nodeB] - 2 * self.distances[lca]

    # targetNodeが2つのノード間のパス上に存在するかを返す。
    def isOnPath(self, nodeA: int, nodeB: int, evalNode: int):
        """
        O(logN)
        """
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
        u, v = map(int, input().split())
        ld.addEdge(u - 1, v - 1, 1)
        ld.addEdge(v - 1, u - 1, 1)
    ld.build()
    imos = [0] * N

    def dfs(pre: int, now: int):
        for _, next in ld.G[now]: 
            if next == pre: 
                continue
            dfs(now, next)
        if pre != -1:
            imos[pre] += imos[now]
        return

    Q = int(input())
    for i in range(Q):
        a, b = map(int, input().split())
        imos[a - 1] += 1
        imos[b - 1] += 1
        lc = ld.getLca(a - 1, b - 1)
        imos[lc] -= 1 # 辺に加算したいならimos[lc] -= 2としてp_lcの処理はいらない。
        p_lc = ld.upstream(lc, 1)
        if p_lc != -1:
            imos[p_lc] -= 1
    dfs(-1, 0)
    ans = 0
    for num in imos:
        ans += num * (num + 1) // 2
    print(ans)
    return
        
if __name__ == '__main__':
    main()