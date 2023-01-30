#!/usr/bin/env python3
import sys
INF = 10 ** 16

class BellmanFord():
    def __init__(self, N: int) -> None:
        self.N = N 
        self.E: "list[tuple(int, int, int)]" = []
        return
    
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.E.append((fromNode, toNode, cost))
        # print("Really directed Graph?")
        return
    
    def build(self, startNode: int):
        dist = [INF] * self.N
        dist[startNode] = 0
        # 少なくとも頂点数N回だけ全部の辺について最短手数を更新すれば最短経路がもとまる。 O(V * E)
        # N + 1回目に更新が発生するということは閉路があるということなので、そこから到達可能な辺は全て影響を受けることから=INFで潰す。 O(N * E)
        for i in range(self.N * 2):
            for fromNode, toNode, cost in self.E:
                if dist[fromNode] != INF and dist[toNode] > dist[fromNode] + cost:
                    if i >= self.N - 1:
                        dist[toNode] = -INF
                    else:
                        dist[toNode] = dist[fromNode] + cost
        return dist

def solve(N: int, M: int, P: int, A: "List[int]", B: "List[int]", C: "List[int]"):
    bf = BellmanFord(N)
    for aa, bb, cc in zip(A, B, C):
        bf.addEdge(aa - 1, bb - 1, -cc + P) 
    
    c = bf.build(startNode=0)
    if c[-1] == -INF:
        print(-1)
        return
    if c[-1] >= 0:
        print(0)
        return
    print(-c[-1])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    solve(N, M, P, A, B, C)

if __name__ == '__main__':
    main()
