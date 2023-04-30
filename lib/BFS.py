# ------------------------------------------------------------------------------
#     BFS (グラフ)
# ------------------------------------------------------------------------------
# Input
#   1. 隣接リスト
#   2. 開始ノード
# Order
#   O(V + E)
# Output
#   スタートから各ノードへの最小コスト
# verify
#  省略 検証済み
# ------------------------------------------------------------------------------
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

# Note :
#
# distの次元を拡張する場合、dp的にfor hop for nextの2重で回してもいいがqueueに入れた方が早くてバグらないかも
# dist[start_node][0] = 0
# q.append((start_node, 0))
# while q:
#     now, now_step = q.popleft()
#     for next in G[now]:
#         if dist[next][(now_step + 1) % 3] != INF:
#             continue
#         q.append((next, (now_step + 1) % 3))
#         dist[next][(now_step + 1) % 3] = dist[now][now_step] + 1
# return dist

# ------------------------------------------------------------------------------
#     BFS (グリッド)
# ------------------------------------------------------------------------------
# Input
#   1. 全てのマスが隣接したフィールドの二次元配列
#   2. 1の高さ
#   3. 1の幅
#   4. スタート地点のy座標
#   5. スタート地点のx座標
# Output
#   スタートから各ノードへの最小コスト
# Order
#    O(V + E)
# Note
#   開始点が壁の場合には除く必要あり。
# verify
#  省略 検証済み
# ------------------------------------------------------------------------------
from collections import deque
def bfs(G, H, W, startY, startX) -> list:
    # ゴールやスタートを任意に設定できる問題では開始点が壁であるケースに注意!!!!
    INF = 10 ** 16
    q = deque()
    dist = [[INF] * W for _ in range(H)]
    q.append((startY, startX))
    dist[startY][startX] = 0
    while q:
        nowy, nowx = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nexty = nowy + dy
            nextx = nowx + dx
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != INF or G[nexty][nextx] == "#":
                continue
            q.append((nexty, nextx))
            dist[nexty][nextx] = dist[nowy][nowx] + 1
    return dist

# ------------------------------------------------------------------------------
#     多始点BFS (グラフ)
# ------------------------------------------------------------------------------
# Input
#   1. 隣接リスト
#   2. 開始ノード
# Order
#   O(V + E)
# Output
#   スタートから各ノードへの最小コスト
# verify
#  未検証
# ------------------------------------------------------------------------------
def multiStartBfs(G: "List[to]", start_nodes: "List[int]") -> list:
    from collections import deque
    INF = 10 ** 16
    q = deque()
    dist = [INF] * len(G)
    for start_node in start_nodes:
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

# ------------------------------------------------------------------------------
#     多始点BFS (グリッド)
# ------------------------------------------------------------------------------
# Input
#   1. 全てのマスが隣接したフィールドの二次元配列
#   2. 1の高さ
#   3. 1の幅
#   4. スタート地点のy座標
#   5. スタート地点のx座標
# Output
#   スタートから各ノードへの最小コスト
# Order
#    O(V + E)
# Note
#   開始点が壁の場合には除く必要あり。
# verify
#  未検証
# ------------------------------------------------------------------------------
def multiStartBfs(G, H, W, startPoints: "List[set(startY, startX)]") -> list:
        from collections import deque
        INF = 10 ** 16
        q = deque()
        dist = [[INF] * W for _ in range(H)]
        for startY, startX in startPoints:
            q.append((startY, startX))
            dist[startY][startX] = 0
        while q:
            nowy, nowx = q.popleft()
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nexty = nowy + dy
                nextx = nowx + dx
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != INF or G[nexty][nextx] == "#":
                    continue
                q.append((nexty, nextx))
                dist[nexty][nextx] = dist[nowy][nowx] + 1
        return dist

##
## 0/1BFS


from collections import deque
def bfs01(G, H, W, startY, startX) -> list:
    # ゴールやスタートを任意に設定できる問題では開始点が壁であるケースに注意!!!!
    INF = 10 ** 16
    q = deque()
    q.append((startY, startX))
    count = [[INF] * W for _ in range(H)]
    count[startY][startX] = 0
    while q:
        nowy, nowx = q.popleft()
        for dx in range(-2, 2 + 1):
            for dy in range(-2, 2 + 1):
                nexty = nowy + dy
                nextx = nowx + dx
                if (dx, dy) == (0, 0): 
                    continue
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or G[nexty][nextx] == "#":
                    continue
                # 特殊な移動をしない
                if (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if count[nexty][nextx] > count[nowy][nowx]:
                        count[nexty][nextx] = count[nowy][nowx]
                        q.appendleft((nexty, nextx))
                # 特殊な移動をする
                else:  
                    if count[nexty][nextx] > count[nowy][nowx] + 1:
                        count[nexty][nextx] = count[nowy][nowx] + 1
                        q.append((nexty, nextx))
    return count
    