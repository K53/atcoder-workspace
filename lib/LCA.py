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
# - 応用
#   - https://yukicoder.me/submissions/699828 (ノードにコストが与えられた問題 : BFSしてからLCA)
# ------------------------------------------------------------------------------
class LcaDoubling:
    # 木であれば任意の点を根と見做せる。
    def __init__(self, N, root=0):
        print("有向辺でLCAする場合、根rootを明示的に指定すること。出次数0のノードで終了し不整合となる。")
        self.N = N
        self.root = root
        self.G = [[] for _ in range(N)]
        self.depths = [-1] * N
        self.distances = [-1] * N
        self.ancestors = [] # ダブリングによって求めた祖先の配列の配列 i番目の配列は過去ノードの2^i個祖先のノードを格納する。
        return
    
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        print("Really directed Graph?")
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

# Usage
N = 5
edges = [(1, 2), (1, 3), (1, 4), (4, 5)]
ld = LcaDoubling(N)
for a, b in edges:
    ld.addEdge(fromNode=a - 1, toNode=b - 1, cost=1)
    ld.addEdge(fromNode=b - 1, toNode=a - 1, cost=1)
ld.build()
print(ld.ancestors)
"-> [[-1, 0, 0, 0, 3, -1], [-1, -1, -1, -1, 0, -1]]"
    # ↑                     ↑
    # 各ノードの2^0個上       各ノードの2^1個上
print(ld.getLca(1, 2)) # LCAを出力
"-> 0"
print(ld.getDistance(1, 2)) # 2つのノード間の距離を出力。
"-> 2"

print(ld.isOnPath(nodeA=0, nodeB=4, evalNode=3)) # True
