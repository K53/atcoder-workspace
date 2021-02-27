#!/usr/bin/env python3
import heapq
INF = 10 ** 13
MOD = 28

def dijkstra(edges: "List[List[(cost, to)]]", start_node: int, init_modcost: int):
    N = len(edges)
    hq = []
    heapq.heapify(hq)
    # Set start info
    # dist[i][c] := 経過時間をMODで割った余りがcとなる時点で町iにいるための最短コスト
    dist = [[INF] * (MOD + 1) for _ in range(N)]
    heapq.heappush(hq, (0, start_node, init_modcost))
    dist[start_node][init_modcost] = 0
    # dijkstra
    while hq:
        min_cost, node_now, modcost_now = heapq.heappop(hq)
        # いつも通り、既に最短コストのパスが発見されているならスキップ
        if min_cost > dist[node_now][modcost_now]:
            continue

        # 一度ゴールに着いたら戻れない
        if node_now == N - 1:
            continue

        # 辺の通過
        for cost, next in edges[node_now]: 
            modcost_next = (modcost_now + cost) % MOD
            if dist[next][modcost_next] > min_cost + cost:             # いつも通り
                dist[next][modcost_next] = min_cost + cost
                heapq.heappush(hq, (dist[next][modcost_next], next, modcost_next))
    return dist

def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        f, t, c = map(int, input().split())
        edges[f].append((c, t))
        edges[t].append((c, f))
    dist = dijkstra(edges, 0, 0)
    ans = []
    targets = set(range(0, MOD + 1, 4)) | set(range(0, MOD + 1, 7))
    for i in targets:
        ans.append(dist[N - 1][i])
    print(min(ans))

if __name__ == '__main__':
    main()
