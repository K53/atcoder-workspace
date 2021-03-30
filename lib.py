def bfs(edges: "List[to]", start_node: int) -> list:
    q = queue.Queue()
    dist = [INF] * len(edges)
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


# ----
# 入力受け取り


# ----
# モジュール
import string
# https://docs.python.org/ja/3/library/string.html
print(string.ascii_lowercase)
# >> abcdefghijklmnopqrstuvwxyz

# ----


# --
# 2^N 通りのビット全探索。
for n in range(2 ** N):
    for i in range(N):
        if (n >> i) & 1:
            # i桁目のビットが立っている場合の処理
            pass
# --


# = 最大公約数 / 最小公倍数 ===============================================================
factor1 = factor2 = 1
# 最大公約数
import math
print(math.gcd(factor1, factor2))
# 最小公倍数
print(factor1 * factor2 // math.gcd(factor1, factor2))
# ======================================================================================


# = dijkstra ===========================================================================
# ----------------------------------------------------------------
# Input
#   1. タプル(重み, 行先)の二次元配列(隣接リスト)
#   2. 探索開始ノード(番号)
# Output
#   スタートから各ノードへの最小コスト
# Order
#   O(V + E * logV)
# Note
#   *1 https://atcoder.jp/contests/abc191/tasks/abc191_e
#       - 多始点ダイクストラの場合の注意。
#       - コストの異なる並行な辺がある場合、小さい方を選択する必要あり。
#       - dist[start_node] = min(cost, dist[start_node])
#   *2 https://atcoder.jp/contests/tkppc4-1/tasks/tkppc4_1_h
#       - INFの値は毎回吟味すること。
# ----------------------------------------------------------------
import heapq
INF = 10 ** 9       # *2
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

# Usage

# ======================================================================================


# = bellmanFord ========================================================================
# ----------------------------------------------------------------
# Input
#   1. 辺のリスト: タプル(始点, 終点, 重み)
#   2. 頂点数
#   3. 探索開始ノード(番号)
# Output
#   リスト(スタートから各ノードへの最小コスト。ただし負閉路から到達可能なノードは-INF)
# Order
#   O(V * E)
# Note
#   始点から到達不可能な負閉路の有無： ×　(ベルマンフォード法では発見されない)
#   始点から到達可能だが終点に影響ない負閉路の有無： ○ (出力のリストに-INFが含まれるかどうか)
#   始点から到達可能で終点に到達する負閉路の有無：　○ (出力のリストの終点へのコストが-INFかどうか)
# ----------------------------------------------------------------
INF = 10 ** 16
def bellmanFord(edges: "List[(from, to, to)]", vertex: int, start_node: int) -> list:
    # Initialize
    costs = [INF] * vertex
    costs[start_node] = 0
    # {vertex}回目に更新があるノード = 負閉路の中にある。
    # {vertex + 1}回目からはそのノードを起点として到達可能な箇所を"-INF"で塗りつぶしていく。
    # 即ち、{vertex * 2}回目には全域ノードが網羅され、負閉路から移動可能なノードはすべて"-INF"になっている。
    for i in range(vertex * 2):
        for f, t, c in edges:
            if costs[f] != INF and costs[t] > costs[f] + c:
                if i >= vertex - 1:
                    costs[t] = -INF
                else:
                    costs[t] = costs[f] + c
    return costs
# ======================================================================================


# = LCS ================================================================================
# 長さだけ欲しい
# ----------------------------------------------------------------
# Input
#   1. 文字列1
#   2. 文字列2
# Output
#   最長共通部分列の長さ
# Order
#   O(len(string_length))
#   string_length : 小さい方の文字列の長さ
# Note
#   L[i] =: 文字列aのj文字目までと文字列bのbkまでから長さがi+1の共通部分列が作れるときjが取る最小値
# ----------------------------------------------------------------
def getLengthOfLcs(a: str, b: str):
    L = []
    for bk in b:
        bgn_idx = 0  # 検索開始位置
        for i, cur_idx in enumerate(L):
            # ※1
            chr_idx = a.find(bk, bgn_idx) + 1
            if not chr_idx:
                break
            L[i] = min(cur_idx, chr_idx)
            bgn_idx = cur_idx
        else:
            # ※2
            chr_idx = a.find(bk, bgn_idx) + 1
            if chr_idx:
                L.append(chr_idx)
    return len(L)
# ======================================================================================
# 文字列を欲しい
# ----------------------------------------------------------------
# Input
#   1. 文字列1
#   2. 文字列2
# Output
#   最長共通部分列の長さ
# Order
#   O(len(b))
# Note
#   dp[s][t] =: 文字列str1のs文字目までと文字列str2のt文字目までのLCS。(0 <= s < len(str1), 0 <= t < len(str2))
#   例)
#   axyb      (str1)
#   abyxb     (str2)
#   生成するdp
#   [1, 1, 1, 1, 1]
#   [1, 1, 1, 2, 2]
#   [1, 1, 2, 2, 2]
#   [1, 2, 2, 2, 3]
# ----------------------------------------------------------------

def getLcs(str1: str, str2: str):
    ls1, ls2 = len(str1), len(str2)
    dp = []
    for _ in range(ls1):
        dp.append([0] * (ls2))
    
    # str1の0文字目の初期化
    isSameFound = False
    for t in range(ls2):
        if isSameFound or str2[t] == str1[0]:
            dp[0][t] = 1
            isSameFound = True

    # str2の0文字目の初期化
    isSameFound = False
    for s in range(ls1):
        if isSameFound or str1[s] == str2[0]:
            dp[s][0] = 1
            isSameFound = True

    for s in range(1, ls1):
        for t in range(1, ls2):
            dp[s][t] = dp[s - 1][t - 1] + 1 if str1[s] == str2[t] else max(dp[s][t - 1], dp[s - 1][t])
    
    # for a in range(ls1):
    #     print(dp[a])
    s, t = ls1 - 1, ls2 - 1
    lcs = ""
    while s >= 0 and t >= 0:
        if str1[s] == str2[t]:
            lcs += str1[s]
            s -= 1
            t -= 1
        else:
            if s == 0:
                t -= 1
            elif t == 0:
                s -= 1
            elif dp[s-1][t] > dp[s][t-1]:
                s -= 1
            else:
                t -= 1
    return lcs[::-1]
# ======================================================================================

# = 約数列挙 ============================================================================
# ----------------------------------------------------------------
# Input
#   1. 約数を求めたい数
# Output
#   約数リスト(昇順)
# Order
#   O(√n)
# ----------------------------------------------------------------
def getDivisors(n: int):
    # validation check
    # if not isinstance(n, int):
    #     raise("[ERROR] parameter must be integer")
    # if n < 0:
    #     raise("[ERROR] parameter must be not less than 0 (n >= 0)")

    lowerDivisors, upperDivisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lowerDivisors.append(i)
            if i != n // i:
                upperDivisors.append(n//i)
        i += 1
    return lowerDivisors + upperDivisors[::-1]
# ======================================================================================


# = 組み合わせ ===========================================================================
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
 
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    # print(numerator)
    # print("----------")
    # print(denominator)
    # print("")
    for p in range(2,r + 1):                    # p番目について、
        pivot = denominator[p - 1]              # pivotで約分を試みる。
        # print("--- p  : " + str(p))
        # print("--- piv: " + str(pivot))
        if pivot > 1:                           # ただし、pivotが1、すなわちすでに割り尽くされているならp番目は飛ばす。
            offset = (n - r) % p
            # print("--- off: " + str(offset))
            for k in range(p-1,r,p):            # p番目を約分できるということはp番目からpの倍数番目も約分かのうなので実施する。
                # print("------ for " + str(k) + " in range(" + str(p-1) + "," + str(r) + "," + str(p) + ")")
                # print("------ numerator[k - offset]: " + str(numerator[k - offset]))
                # print("------ denominator[k]       : " + str(denominator[k]))
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
 
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
 
    return result
# ======================================================================================

# = 直交座標/極座標 変換 ==================================================================
import math
# 直交座標 → 極座標
def toPolarCoordinates(taeget_x, taeget_y, origin_x = 0, origin_y = 0) -> ("distance", "radian"):
    _x, _y = taeget_x - origin_x, taeget_y - origin_y
    r = math.sqrt(_x ** 2 + _y ** 2)
    rad = math.atan2(_y, _x)
    return (r, rad)

# 極座標 → 直交座標
def toCartesianCoordinates(r, rad, origin_x = 0, origin_y = 0) -> ("x", "y"):
    x = r * math.cos(rad) + origin_x
    y = r * math.sin(rad) + origin_y
    return (x, y)
# ======================================================================================
