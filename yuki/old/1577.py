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
    compressed = {}
    compressed_to_row = []
    routes = set(stones)
    for index, val in enumerate(sorted(list(routes))):
        compressed[val] = index
        compressed_to_row.append(val)
    # print(compressed)
    G = [[] for _ in range(N + 2)]
    for i in range(N + 2):
        for b in range(30):
            reachable = stones[i] ^ 1 << b
            if reachable in compressed:
                G[compressed[stones[i]]].append(compressed[reachable])
                G[compressed[reachable]].append(compressed[stones[i]])
    d = bfs(G, compressed[st])
    print(d[compressed[ed]] - 1 if d[compressed[ed]] != INF else -1)
    return

if __name__ == '__main__':
    main()