#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def main():
    N = int(sys.stdin.readline())
    a, b = map(int, sys.stdin.readline().split())
    M = int(sys.stdin.readline())
    G = [[] for _ in range(N)]
    xy = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
    for x, y in xy:
        G[x - 1].append(y - 1)
        G[y - 1].append(x - 1)

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
    d = bfs(G, a - 1)
    # print(d)
    GG = [[] for _ in range(N)]
    for xx, yy in xy:
        if d[xx - 1] - d[yy - 1] == 1:
            GG[yy - 1].append(xx - 1)
        if d[xx - 1] - d[yy - 1] == -1:
            GG[xx - 1].append(yy - 1)
    
    # print(GG)
    sys.setrecursionlimit(10 ** 9)
    seen = [False] * N
    # firstOrder = []
    # lastOrder = []
    ans = 0
    def dfs(G: "list[list[int]]", now: int):
        nonlocal ans
        # firstOrder.append(now)
        seen[now] = True
        for next in G[now]:
            # if seen[next]:
            #     continue
            dfs(G, next)
        # lastOrder.append(now)
        if now == b - 1:
            ans += 1
            ans %= MOD
    
    dfs(GG, a - 1)
    print(ans % MOD)
    return




if __name__ == '__main__':
    main()
