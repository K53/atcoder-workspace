# ------------------------------------------------------------------------------
#     最大流 (FordFulkerson)
# ------------------------------------------------------------------------------
# 解説
# - DFSで始点から終点に到達可能な経路を探索し、その経路の中でもっとも小さい容量を流量として確定する。
# - この時、求めた経路の各辺に確定した流量と同値の逆辺を張る。
# - この処理をDFSの解が得られなくなるまで繰り返す。
# 
# リンク
# - https://tjkendev.github.io/procon-library/python/max_flow/ford-fulkerson.html
# - https://even-eko.hatenablog.com/entry/2013/08/08/195120
# - 逆辺の必要性は蟻本の解説がわかりやすい。
# 
# Order
#   O(FE) ・・・ DFS実行回数F×辺数E
#
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=ja
# ------------------------------------------------------------------------------
INF = 10 ** 9
class FordFulkerson:
    def __init__(self, N):
        self.N = N
        # グラフGでは、そのノードfromNodeから到達可能な各ノードについて、[toNode, Capacity, [逆辺用のfromNodeの情報]]が含まれる。
        # G[fromNode] = [toNode, capacity, [fromNode, capacity, [...]]] # 循環参照のためGを出力すると無限に続く。
        self.G = [[] for _ in range(N)] 

    def addEdge(self, fromNode, toNode, capacity):
        forward = [toNode, capacity, None]
        forward[2] = backward = [fromNode, 0, forward]
        self.G[fromNode].append(forward)
        self.G[toNode].append(backward)

    # def add_multi_edge(self, v1, v2, cap1, cap2):
    #     edge1 = [v2, cap1, None]
    #     edge1[2] = edge2 = [v1, cap2, edge1]
    #     self.G[v1].append(edge1)
    #     self.G[v2].append(edge2)

    def dfs(self, now, dist, flow):
        if now == dist:
            return flow
        seen = self.seen
        seen[now] = True
        for forwardEdge in self.G[now]:
            nextNode, capacity, revEdge = forwardEdge
            if capacity > 0 and not seen[nextNode]:
                decidedFlow = self.dfs(nextNode, dist, min(flow, capacity))
                if decidedFlow:
                    forwardEdge[1] -= decidedFlow
                    revEdge[1] += decidedFlow
                    return decidedFlow
        return 0

    def flow(self, s, t):
        flow = 0
        f = INF
        N = self.N
        while f:
            self.seen = [0] * N
            f = self.dfs(s, t, INF)
            flow += f
        return flow


N = 4
Edges = [(0, 1, 2), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 3, 2)]
ff = FordFulkerson(N)
for e in Edges:
    ff.addEdge(*e)
f = ff.flow(0, N - 1)
print(f)
"-> 3"







