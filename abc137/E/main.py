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

def main():
    N, M, P = map(int, input().split())
    edges = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a - 1, b - 1, -(c - P)))

    costs = bellmanFord(edges, N, 0)
    if costs is None or costs[-1] == -INF:
        print(-1)
        return

    print(0 if costs[N - 1] > 0 else -costs[N - 1])
    return

if __name__ == '__main__':
    main()
