#!/usr/bin/env python3

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A&lang=ja

INF = 10 ** 9
class FordFulkerson:
    def __init__(self, N):
        self.N = N
        self.G = [[] for i in range(N)] # G[fromNode] = [toNode, capacity, [fromNode, capacity, []]]

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

def main():
    N, M = map(int, input().split())
    ff = FordFulkerson(N)
    for _ in range(M):
        f, t, c = map(int, input().split())
        ff.addEdge(f, t, c)
    ans = ff.flow(0, N - 1)
    print(ans)

    
if __name__ == '__main__':
    main()

