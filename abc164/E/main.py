#!/usr/bin/env python3
import sys
import heapq
INF = 10 ** 13
SILVER_MAX = 2500

def dijkstra(edges: "List[List[(cost, to, silver)]]", C: "List[int]", D: "List[int]", start_node: int, init_silver: int):
    hq = []
    heapq.heapify(hq)
    # Set start info
    # dist[i][s] := 銀貨をs枚持った状態で頂点iに到達する時のコスト
    dist = [[INF] * (SILVER_MAX + 1) for _ in range(len(edges))]
    heapq.heappush(hq, (0, start_node, init_silver))
    dist[start_node][init_silver] = 0
    
    # dijkstra
    while hq:
        min_cost, node_now, silver_now = heapq.heappop(hq)
        # いつも通り、既に最短コストのパスが発見されているならスキップ
        if min_cost > dist[node_now][silver_now]:
            continue

        # 補充(状態変化)
        # 2500枚を超えて銀貨に換える必要がないためフィルタ
        if silver_now + C[node_now] <= SILVER_MAX:
            # 交換後の銀貨の枚数
            silver_next = silver_now + C[node_now]
            if dist[node_now][silver_next] > min_cost + D[node_now]:    # 交換にかかる時間を加味して比較。そこで交換する方がいいか判定。
                dist[node_now][silver_next] = min_cost + D[node_now]
                heapq.heappush(hq, (dist[node_now][silver_next], node_now, silver_next))

        # 辺の通過
        # 駅を移動するのに銀貨を消費する。
        for cost, next, silver in edges[node_now]: 
            remain_silver = min(silver_now - silver, SILVER_MAX)
            if remain_silver < 0:                                       # 手持ちの銀貨で移動不可ならスキップ
                continue
               
            if dist[next][remain_silver] > min_cost + cost:             # いつも通り
                dist[next][remain_silver] = min_cost + cost
                heapq.heappush(hq, (dist[next][remain_silver], next, remain_silver))
    return dist

def main():
    N, M, S = map(int, input().split())
    init_silver = min(S, SILVER_MAX)

    edges = [[] for _ in range(N)]
    for _ in range(M):
        u, v, a, b = map(int, input().split())
        edges[u - 1].append((b, v - 1, a))
        edges[v - 1].append((b, u - 1, a))
    C, D = [], []
    for i in range(N):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    
    dist = dijkstra(edges, C, D, 0, init_silver)
    print(*[min(d) for d in dist[1:]], sep="\n")

if __name__ == '__main__':
    main()
