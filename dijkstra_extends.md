# ダイクストラの応用問題達

## 待ち時間/乗り換え時間を考慮する

いずれも辺のコストに帰着させることができる。

1. [ABC192 E - Train](https://atcoder.jp/contests/abc192/tasks/abc192_e)
2. [技術室奥プログラミングコンテスト#4 Day1 H - don't be late](https://atcoder.jp/contests/tkppc4-1/tasks/tkppc4_1_h)



```python:問題例2
import heapq
INF = 10 ** 16

def dijkstra(edges: "List[List[(cost, departure, to)]]", start_node: int) -> list:
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    heapq.heappush(hq, (0, start_node))
    dist[start_node] = 0
    # dijkstra
    while hq:
        min_cost, now = heapq.heappop(hq)
        if min_cost > dist[now]:
            continue
        for cost, departure, next in edges[now]:
            rest = 0 if min_cost % departure == 0 else departure - min_cost % departure # あと何分待つか求めて
            if dist[next] > dist[now] + cost + rest:                                    # 次のノードの到着時刻
                dist[next] = dist[now] + cost + rest                                    # に加算する。
                heapq.heappush(hq, (dist[next], next))
    return dist

def main():
    N, M, K = map(int, input().split())
    t = [0] + [int(input()) for _ in range(N - 2)] + [0]
    edges = [[] for _ in range(N)]
    for i in range(M):
        a, b, c, d = map(int, input().split())
        edges[a - 1].append((c + t[b - 1], d, b - 1))       # 乗り換え時間は次の駅への移動時間に追加したらいい
        edges[b - 1].append((c + t[a - 1], d, a - 1))
    d = dijkstra(edges, 0)
    print(d[N - 1] if d[N - 1] <= K else -1)

if __name__ == '__main__':
    main()
```



## 経由地を考慮する/往復する

無向グラフのダイクストラは始点から始めても終点から始めても同じコストになることに注目する。
始点sから経由地iを通って終点tに移動するコストは、始点sから経由地iに移動するコストと終点tから経由地iに移動するコストの和に等しくなる。

1. [ABC035 D - トレジャーハント](https://atcoder.jp/contests/abc035/tasks/abc035_d)
2. [SoundHound Inc. Programming Contest 2018 -Masters Tournament--D Saving Snuuk](https://atcoder.jp/contests/soundhound2018-summer-qual/tasks/soundhound2018_summer_qual_d)



```python:問題例1
def main():
    N, M, T = map(int, input().split())
    A =list(map(int, input().split()))
    edges = [[] for _ in range(N)]
    edges_inv = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a - 1].append((c, b - 1))
        edges_inv[b - 1].append((c, a - 1))
    
    cost1 = dijkstra(edges, 0)
    cost2 = dijkstra(edges_inv, 0)
    ans = 0
    for i in range(N):
        cost = cost1[i] + cost2[i]
        if T - cost < 0:
            continue
        ans = max(ans, (T - cost) * A[i])
    print(ans)

if __name__ == '__main__':
    main()
```

```python:問題例2
def main():
    n, m, s, t = map(int, input().split())
    yen_edges = [[] for _ in range(n)]
    snuuk_edges = [[] for _ in range(n)]
    for _ in range(m):
        u, v, a, b = map(int, input().split())
        yen_edges[v - 1].append((a, u - 1))
        yen_edges[u - 1].append((a, v - 1))
        snuuk_edges[v - 1].append((b, u - 1))
        snuuk_edges[u - 1].append((b, v - 1))
    yd = dijkstra(yen_edges, s - 1)
    sd = dijkstra(snuuk_edges, t - 1)
    cost_min = INF
    ans = []
    for i in reversed(range(n)):
        cost_via_i = yd[i] + sd[i]
        cost_min = min(cost_min, cost_via_i)
        ans.append(10 ** 15 - cost_min)
    print(*reversed(ans), sep="\n")
        
if __name__ == '__main__':
    main()
```



## 頂点倍加

ダイクストラでは複数の状態を同時に扱うことができない。
例えば、町を移動する時にかかる時間と料金を同時に考慮しながら最短経路を求めることができない。
そこで、同じ町にいても所持金が違う場合(状態が違う場合)を異なる頂点と見なして頂点を増やすことで対応する。

単純に頂点を増やしていくとTLEするので、それ以上探索する必要のないステートがないかを探して上限を決める。
この解説がしっくりきた。
https://blog.hamayanhamayan.com/entry/2020/04/26/232132

1. [ABC164 E - Two Currencies](https://atcoder.jp/contests/abc164/tasks/abc164_e)
2. [いろはちゃんコンテスト Day2 G - 通学路](https://atcoder.jp/contests/iroha2019-day2/tasks/iroha2019_day2_g)
3. [AOJ Highway Express Bus](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0212)
4. [WUPC 2012 E - 会場への道](https://atcoder.jp/contests/wupc2012/tasks/wupc2012_5)



```python:問題例1
# どの駅にいるかの他、銀貨を何枚持っているかの情報が必要。
# 全ての辺で銀貨を最大量求められたとしても2500枚あれば足りるので、それを上限として頂点倍加。
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
```

```python:問題例2
# どの駅にいるかの他、何本花を持っているかの頂点の情報が入ってくるので頂点倍加。
# 花はK本以上持っていたら買う必要はないのでKを上限として倍加する。
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
```

```python:問題例3
import heapq
import queue
INF = 10 ** 12

def dijkstra(edges: "List[List[(cost, to)]]", start_node: int, init_coupon: int):
    hq = []
    heapq.heapify(hq)
    # Set start info
    # dist[i][c] := 割引券をc枚持った状態で町iに到達する時のコスト
    dist = [[INF] * (init_coupon + 1) for _ in range(len(edges))]
    heapq.heappush(hq, (0, start_node, init_coupon))
    dist[start_node][init_coupon] = 0
    
    # dijkstra
    while hq:
        min_cost, node_now, coupon_now = heapq.heappop(hq)
        # いつも通り、既に最短コストのパスが発見されているならスキップ
        if min_cost > dist[node_now][coupon_now]:
            continue

        # 辺の通過
        for cost, next in edges[node_now]: 
            if coupon_now > 0:                                          # 割引券を使うパス
                if dist[next][coupon_now - 1] > min_cost + cost // 2:
                    dist[next][coupon_now - 1] = min_cost + cost // 2
                    heapq.heappush(hq, (dist[next][coupon_now - 1], next, coupon_now - 1))
               
            if dist[next][coupon_now] > min_cost + cost:                # いつも通り(割引しないパス)
                dist[next][coupon_now] = min_cost + cost
                heapq.heappush(hq, (dist[next][coupon_now], next, coupon_now))
    return dist

def main():
    while True:
        c, n, m, s, d = map(int, input().split())
        if c == n == m == s == d == 0:
            break
        edges = [[] for _ in range(n)]
        for _ in range(m):
            a, b, f = map(int, input().split())
            edges[a - 1].append((f, b - 1))
            edges[b - 1].append((f, a - 1))

        dist = dijkstra(edges, s - 1, c)
        print(min(dist[d - 1]))

if __name__ == '__main__':
    main()
```

```python:問題例4
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
```



__考え方__

```python:(ABC164Eを例として)
# (1) 必要になるパラメータを受け取る。
def dijkstra(edges: "List[List[(cost, to, silver)]]", C: "List[int]", D: "List[int]", start_node: int, init_silver: int):
    hq = []
    heapq.heapify(hq)
    # Set start info
    # (2) コスト一覧を定義する。    ※ 必ず上限を設定した方がいい。
    # dist[i][s] := 銀貨をs枚持った状態で頂点iに到達する時のコスト
    dist = [[INF] * (SILVER_MAX + 1) for _ in range(len(edges))]
    heapq.heappush(hq, (0, start_node, init_silver))
    dist[start_node][init_silver] = 0                                   # (3) 始点の初期化                          
    
    # dijkstra
    while hq:
        min_cost, node_now, silver_now = heapq.heappop(hq)
        if min_cost > dist[node_now][silver_now]:
            continue

        # 補充(状態変化)                                                  # (4) 補充操作がない場合は削除
        # 2500枚を超えて銀貨に換える必要がないためフィルタ                      # (5) 条件がない場合はフィルタ不要
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
            # 手持ちの銀貨で移動不可ならスキップ
            if remain_silver < 0:                                       # (6) スキップする条件
                continue
               
            if dist[next][remain_silver] > min_cost + cost:             # いつも通り
                dist[next][remain_silver] = min_cost + cost
                heapq.heappush(hq, (dist[next][remain_silver], next, remain_silver))
    return dist
```

## 他

### ■ BFSとの複合問題

1. [第１５回日本情報オリンピック 予選 E - ゾンビ島 (Zombie Island)](https://atcoder.jp/contests/joi2016yo/tasks/joi2016yo_e)



```python
#!/usr/bin/env python3
import heapq
import queue
INF = 10 ** 12

def multiStartBfs(edges: "List[to]", start_nodes: "List[int]") -> list:
    q = queue.Queue()
    dist = [INF] * len(edges)
    for start_node in start_nodes:
        q.put(start_node)
        dist[start_node] = 0
    while not q.empty():
        now = q.get()
        for next in edges[now]:
            if dist[next] != INF:
                continue
            q.put(next)
            dist[next] = dist[now] + 1
    return dist

def dijkstra(edges: "List[List[(cost, to)]]", start_node: int) -> list:
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    heapq.heappush(hq, (0, start_node))
    dist[start_node] = 0
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

def main():
    N, M, K, S = map(int, input().split())
    P, Q = map(int, input().split())
    C = [int(input()) - 1 for _ in range(K)]
    edges = [[] for _ in range(N)]
    edgesWithCost = [[] for _ in range(N)]
    A, B = [], []
    for _ in range(M):
        a, b = map(lambda i : int(i) - 1, input().split())
        A.append(a)
        B.append(b)
        edges[a].append(b)
        edges[b].append(a)
    dangerous = multiStartBfs(edges, C)
    for i in range(M):
        def getCost(node):
            if node == N - 1:
                return 0
            return Q if dangerous[node] <= S else P

        edgesWithCost[A[i]].append((getCost(B[i]), B[i]))
        edgesWithCost[B[i]].append((getCost(A[i]), A[i]))
    for i in C:
        edgesWithCost[i] = []
    d = dijkstra(edgesWithCost, 0)
    print(d[N - 1])

if __name__ == '__main__':
    main()
```



### ■ 多始点ダイクストラ

1. [ABC191 E - Come Back Quickly](https://atcoder.jp/contests/abc191/tasks/abc191_e)



```python
#!/usr/bin/env python3
import heapq
INF = 10 ** 9

def multiDijkstra(edges: "List[List[(cost, to)]]", start: "(cost, to)"):
    hq = []
    heapq.heapify(hq)
    # Set start info
    dist = [INF] * len(edges)
    for cost, to in edges[start]:
        heapq.heappush(hq, (cost, to))
        dist[to] = min(cost, dist[to])
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

def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a - 1].append((c, b - 1))
    
    for start in range(N):
        # set start info
        dist = multiDijkstra(edges, start)
        print(-1 if dist[start] == INF else dist[start])
    return

if __name__ == '__main__':
    main()
```

