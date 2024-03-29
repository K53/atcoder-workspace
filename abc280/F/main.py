#!/usr/bin/env python3
import sys


INF = 10 ** 16
def bellmanFord(edges: "List[(from, to, to)]", vertex: int, start_node: int) -> list:
    # Initialize
    costs = [INF] * vertex
    costs[start_node] = 0
    # {vertex}回目に更新があるノード = 負閉路の中にある。
    # {vertex + 1}回目からはそのノードを起点として到達可能な箇所を"-INF"で塗りつぶしていく。
    # 即ち、{vertex * 2}回目には全域ノードが網羅され、負閉路から移動可能なノードはすべて"-INF"になっている。
    for i in range(vertex * 2):
        for f, t, c in edges:
            if costs[f] != INF and costs[t] > costs[f] + c:
                if i >= vertex - 1:
                    costs[t] = -INF
                else:
                    costs[t] = costs[f] + c
    return costs

def solve(N: int, M: int, Q: int, A: "List[int]", B: "List[int]", C: "List[int]", X: "List[int]", Y: "List[int]"):
    # G = [[] for _ in range(N)]
    # for i in range(M):
    #     G[A[i] - 1].append((B[i] - 1, C[i]))
    #     G[B[i] - 1].append((A[i] - 1, C[i]))
    e = []
    for i in range(M):
        e.append((A[i] - 1, B[i] - 1, C[i]))
        e.append((B[i] - 1, A[i] - 1, -C[i]))

    for i in range(Q):
        ans = bellmanFord(e, N, X[i] - 1)
        res = ans[Y[i] - 1]
        if res == -INF:
            print("inf")
        elif res == INF:
            print("nan")
        else:
            print(res)
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
    Q = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    C = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
    X = [int()] * (Q)  # type: "List[int]"
    Y = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    solve(N, M, Q, A, B, C, X, Y)

if __name__ == '__main__':
    main()
