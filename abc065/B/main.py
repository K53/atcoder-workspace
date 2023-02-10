#!/usr/bin/env python3
import sys
from collections import deque
INF = 10 ** 16
def bfs(G: "List[to]", start_node: int) -> list:
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

def solve(N: int, a: "List[int]"):
    G = [[] for _ in range(N)]
    for i in range(N):
        G[i].append(a[i] - 1)
    d = bfs(G, 0)
    print(-1 if d[1] == INF else d[1])
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, a)

if __name__ == '__main__':
    main()
