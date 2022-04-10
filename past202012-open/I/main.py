#!/usr/bin/env python3


def main():
    N, M, K = map(int, input().split())
    H = list(map(int, input().split()))
    C = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        if H[A - 1] < H[B - 1]:
            G[A - 1].append(B - 1)
        else:
            G[B - 1].append(A - 1)
    from collections import deque
    INF = 10 ** 16
    def bfs(edges: "List[to]", Cs: int) -> list:
        q = deque()
        dist = [INF] * len(edges)
        for cc in C:
            q.append(cc - 1)
            dist[cc - 1] = 0
        while q:
            now = q.popleft()
            for next in edges[now]:
                if dist[next] != INF:
                    continue
                q.append(next)
                dist[next] = dist[now] + 1
        return dist
    d = bfs(G, C)
    for dd in d:
        print(dd if dd != INF else -1)

if __name__ == '__main__':
    main()
