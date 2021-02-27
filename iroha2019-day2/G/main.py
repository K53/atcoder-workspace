#!/usr/bin/env python3
import sys
import heapq
INF = 10 ** 13

def dijkstra(edges: "List[List[(cost, to)]]", K: int, X: "List[int]", Y: "List[int]", start_node: int):
    hq = []
    heapq.heapify(hq)
    # Set start info
    # dist[i][f] := 花をf本以上持った状態で頂点iに到達する時のコスト
    dist = [[INF] * (K + 1) for _ in range(len(edges))]
    init_flower = 0
    heapq.heappush(hq, (0, start_node, init_flower))
    dist[start_node][init_flower] = 0
    
    # dijkstra
    while hq:
        min_cost, node_now, flower_now = heapq.heappop(hq)
        # いつも通り、既に最短コストのパスが発見されているならスキップ
        if min_cost > dist[node_now][flower_now]:
            continue

        # 花購入(状態変化)
        # 上限Kを超えて花を買う必要がないためフィルタ
        if flower_now + X[node_now] <= K:
            # 花を1セット買った後の花の数
            flower_next = flower_now + X[node_now]
            for i in range(flower_next + 1):                    # 今回の問題に関しては1セットの花束でカバーできる範囲全てに移動
                if dist[node_now][i] > min_cost + Y[node_now]:  # 花の購入金額を加味して比較。その花束を買う方がいいか判定。
                    dist[node_now][i] = min_cost + Y[node_now]
                    heapq.heappush(hq, (dist[node_now][i], node_now, i))

        # 辺の通過
        # これまで通り。辺の移動には花の要素が影響しないのでflower_nowのステートのみ見ていればいい。
        for cost, next in edges[node_now]: 
            if dist[next][flower_now] > min_cost + cost:
                dist[next][flower_now] = min_cost + cost
                heapq.heappush(hq, (dist[next][flower_now], next, flower_now))
    return dist

def main():
    N, M, K = map(int, input().split())

    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a - 1].append((c, b - 1))
        edges[b - 1].append((c, a - 1))
    X, Y = [], []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    
    dist = dijkstra(edges, K, X, Y, 0)
    # for i in range(N):
    #     print(dist[i])
    ans = dist[N - 1][K]
    print(-1 if ans == INF else ans)

if __name__ == '__main__':
    main()
