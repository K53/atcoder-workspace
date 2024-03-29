#!/usr/bin/env python3
import sys
from collections import deque
def bfs(G: "List[to]", start_node: int) -> list:
    INF = 10 ** 16
    q = deque()
    dist = [INF] * len(G)
    q.append(start_node)
    dist[start_node] = 0
    while q:
        now = q.popleft()
        for next in G[now]:
            if dist[next] != INF:
                continue
            q.append(next)
            dist[next] = dist[now] + 1
    return dist


def solve(N: int, u: int, v: int, A: "List[int]", B: "List[int]"):
    N = 8
    A = [1,2,3,3,5,4,7]
    B = [2,3,4,5,6,7,8]
    u = 1
    v = 2
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        G[A[i] - 1].append(B[i] - 1)
        G[B[i] - 1].append(A[i] - 1)
    ub = bfs(G, u - 1)
    vb = bfs(G, v - 1)
    print(ub, vb)
    dist = 0
    for i in range(N):
        # print(i, ub, vb)
        if ub[i] < vb[i]:
            dist = max(ub[i] + (vb[i] - ub[i]) // 2, dist)
    print(dist)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = int(next(tokens))  # type: int
    v = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, u, v, A, B)

if __name__ == '__main__':
    main()
