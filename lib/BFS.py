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
def bfs(edges: "List[to]", start_node: int) -> list:
    INF = 10 ** 16
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
def bfs(edges, H, W, startY, startX) -> list:
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
            if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != INF or edges[nexty][nextx] == "#":
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
def multiStartBfs(edges: "List[to]", start_nodes: "List[int]") -> list:
    from collections import deque
    INF = 10 ** 16
    q = deque()
    dist = [INF] * len(edges)
    for start_node in start_nodes:
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
def multiStartBfs(edges, H, W, startPoints: "List[set(startY, startX)]") -> list:
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
                if nexty < 0 or nextx < 0 or nexty >= H or nextx >= W or dist[nexty][nextx] != INF or edges[nexty][nextx] == "#":
                    continue
                q.append((nexty, nextx))
                dist[nexty][nextx] = dist[nowy][nowx] + 1
        return dist
