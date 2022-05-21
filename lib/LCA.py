# ------------------------------------------------------------------------------
#     最小共通祖先(ダブリングver)
# ------------------------------------------------------------------------------
# 解説
# - 2つのノードの共通祖先となるノード、そのほか、任意の2点間の距離を算出可。
# 
# リンク
# - https://algo-logic.info/lca/ 
# - https://www.slideshare.net/chokudai/abc014
# - https://ikatakos.com/pot/programming_algorithm/graph_theory/lowest_common_ancestor
# 
# 計算量
# - O(NlogN) : 前計算
# - O(logN)  : クエリ
# 
# verify
# - getLca()
#   - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_C&lang=ja
#   - https://yukicoder.me/submissions/699828
# - getDistance()
#   - https://atcoder.jp/contests/abc014/tasks/abc014_4
# ------------------------------------------------------------------------------
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
    
    def addEdge(self, a: int, b: int, cost: int):
        self.G[a].append((cost, b))
        print("Really directed Graph?")
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

# Usage
N = 5
edges = [(1, 2), (1, 3), (1, 4), (4, 5)]
ld = LcaDoubling(N)
for a, b in edges:
    ld.addEdge(a - 1, b - 1, cost=1)
    ld.addEdge(b - 1, a - 1, cost=1)
ld.build()
print(ld.getLca(1, 2)) # LCAを出力
"-> 0"
print(ld.getDistance(1, 2)) # 2つのノード間の距離を出力。
"-> 2"