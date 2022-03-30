#!/usr/bin/env python3

def main():
    import math
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
    N = int(input())
    st, ed = map(int, input().split())
    stones = [st] + list(map(int, input().split())) + [ed]
    G = [[] for _ in range(N + 2)]
    for i in range(N + 1):
        for j in range(i + 1, N + 2):
            w = stones[i] ^ stones[j]
            if w == 0 or math.log2(w).is_integer():
                G[i].append(j)
                G[j].append(i)
    d = bfs(G, 0)
    print(d[-1] - 1 if d[-1] != INF else -1)
    return

if __name__ == '__main__':
    main()