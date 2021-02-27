#!/usr/bin/env python3
import sys
import heapq
INF = 10 ** 18
def dijkstra(edges: "List[List[(cost, departure, to)]]", start_node: int) -> list:
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    heapq.heappush(hq, (0, start_node))
    dist[start_node] = 0
    # dijkstra
    while hq:
        min_cost, now = heapq.heappop(hq)
        if min_cost > dist[now]:
            continue
        for cost, departure, next in edges[now]:
            rest = 0 if min_cost % departure == 0 else departure - min_cost % departure
            if dist[next] > dist[now] + cost + rest:
                dist[next] = dist[now] + cost + rest
                heapq.heappush(hq, (dist[next], next))
    return dist

def solve(N: int, M: int, X: int, Y: int, A: "List[int]", B: "List[int]", T: "List[int]", K: "List[int]"):
    edegs = [[] for _ in range(N)]
    for i in range(M):
        a, b, c, st = A[i], B[i], T[i], K[i]
        edegs[a - 1].append((c, st, b - 1))
        edegs[b - 1].append((c, st, a - 1))
    dist = dijkstra(edegs, X - 1)
    # print("###")
    # print(dist)
    ans = dist[Y - 1]
    print(-1 if ans == INF else ans)
    return 


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    T = [int()] * (M)  # type: "List[int]"
    K = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        T[i] = int(next(tokens))
        K[i] = int(next(tokens))
    solve(N, M, X, Y, A, B, T, K)

if __name__ == '__main__':
    main()
