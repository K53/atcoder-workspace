#!/usr/bin/env python3


def main():
    INF = 10 ** 18
    import heapq
    def dijkstra(edges: "List[List[(cost, to)]]", start_node: int) -> list:
        hq = []
        heapq.heapify(hq)
        # Set start info
        dist = [INF] * len(edges)
        heapq.heappush(hq, (0, start_node))
        dist[start_node] = 0            # *1
        # dijkstra
        while hq:
            min_cost, now = heapq.heappop(hq)
            if min_cost > dist[now]:
                continue
            for cost, next in edges[now]:
                if dist[next] > dist[now] + cost:
                    dist[next] = dist[now] + cost
                    heapq.heappush(hq, (dist[next], next))
        return dist
    H, W = map(int, input().split())
    rs, cs = map(lambda i: int(i) - 1, input().split())
    rt, ct = map(lambda i: int(i) - 1, input().split())
    field = []
    for h in range(H):
        for w in input():
            if w == ".":
                

    
    print(bfs(field, H, W, rs, cs)[rt][ct][0])

if __name__ == '__main__':
    main()
