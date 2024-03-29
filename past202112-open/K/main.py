#!/usr/bin/env python3
from dis import dis
import sys
from collections import deque
INF = 10 ** 16
def bfs(edges: "List[to]", start_node: int) -> list:
    q = deque()
    dist = [INF] * len(edges)
    q.append(start_node)
    dist[start_node] = 0
    while q:
        now = q.popleft()
        for next in edges[now]:
            if dist[next] != INF:
                continue
            q.append(next)
            dist[next] = dist[now] + 1
    return dist

def solve(N: int, M: int, Q: int, K: int, a: "List[int]", u: "List[int]", v: "List[int]", s: "List[int]", t: "List[int]"):
    G = [[] for _ in range(N)]
    for i in range(M):
        G[u[i] - 1].append(v[i] - 1)
        G[v[i] - 1].append(u[i] - 1)
    d = []
    for aa in a:
        d.append(bfs(G, aa - 1))
    for ss, tt in zip(s, t):
        ans = INF
        for i in range(K):
            ans = min(ans, d[i][ss - 1] + d[i][tt - 1])
        print(ans)
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
    K = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(K)]  # type: "List[int]"
    u = [int()] * (M)  # type: "List[int]"
    v = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    s = [int()] * (Q)  # type: "List[int]"
    t = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        s[i] = int(next(tokens))
        t[i] = int(next(tokens))
    solve(N, M, Q, K, a, u, v, s, t)

if __name__ == '__main__':
    main()
