#!/usr/bin/env python3
import heapq
INF = 10 ** 9

def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        edge[a - 1].append((c, b - 1))
    for s in range(N):
        h = []
        costs = [INF] * N
        for c, v in edge[s]:
            h.append((c, v))
            costs[v] = min(c, costs[v])
        heapq.heapify(h)
        while len(h) > 0:
            cost, now = heapq.heappop(h)
            if cost > costs[now]:
                continue
            for c, next in edge[now]:
                if costs[next] > costs[now] + c:
                    costs[next] = costs[now] + c
                    heapq.heappush(h, (costs[next], next))
        print(-1 if costs[s] == INF else costs[s])
    return
if __name__ == '__main__':
    main()
