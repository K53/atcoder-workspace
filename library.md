
## 入力受け取り

```python
# ---------
# マス目
# ---------
H, W = map(int, input().split())
unOverwritableList = []
overwritableList = []
for _ in range(H):
    unOverwritableList.append(input())
    overwritableList.append(list(input()))
print(unOverwritableList)   # ['.....', '.###.', '.###.', '.###.', '.....']
print(overwritableList)     # [['.', '.', '.', '.', '.'], ['.', '#', '#', '#', '.'], ['.', '#', '#', '#', '.'], ['.', '#', '#', '#', '.'], ['.', '.', '.', '.', '.']]
unOverwritableList[0][0] = "a"   # 置き換え不可
overwritableList[0][0] = "a"   # 置き換え可能
```

## モジュール

```python
import string
# https://docs.python.org/ja/3/library/string.html
print(string.ascii_lowercase)
# >> abcdefghijklmnopqrstuvwxyz
```

## 探索

### ビット全探索

```python
# 2^N 通りのビット全探索。
for n in range(2 ** N):
    for i in range(N):
        if (n >> i) & 1:
            # i桁目のビットが立っている場合の処理
            pass
```

### BFS

```python
# = bfs(隣接) ===========================================================================
# ----------------------------------------------------------------
# Input
#   1. 全てのマスが隣接したフィールドの二次元配列
#   2. 1の高さ
#   3. 1の幅
#   4. スタート地点のy座標
#   5. スタート地点のx座標
# Output
#   スタートから各ノードへの最小コスト
# Order
#   
# Note
#   開始点が壁の場合には除く必要あり。
# ----------------------------------------------------------------
import queue
INF = 10 ** 9
def bfs(field: "List[Lsit[]]", H: int, W: int, y: int, x: int) -> list:
    q = queue.Queue()
    dist = []
    for _ in range(H):
        dist.append([-INF] * W)
    q.put((x, y))
    dist[y][x] = 0
    while not q.empty():
        now_x, now_y= q.get()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_x, next_y = now_x + dx, now_y + dy
            if next_y < 0 or next_y >= H or next_x < 0 or next_x >= W or field[next_y][next_x] == "#" or dist[next_y][next_x] != -INF:
                continue
            q.put((next_x, next_y))
            dist[next_y][next_x] = dist[now_y][now_x] + 1
    return dist
# ======================================================================================
```

## 動的計画法

### dijkstra

```python
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
```


### bellmanFord

```python
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
```


### LCS

```python
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
```

## 数学

### 最大公約数/最小公倍数

```python
# = 最大公約数 / 最小公倍数 ===============================================================
factor1 = factor2 = 1
# 最大公約数
import math
print(math.gcd(factor1, factor2))
# 最小公倍数
print(factor1 * factor2 // math.gcd(factor1, factor2))
# ======================================================================================
```

### 素数判定

```python
# = 素数判定 ============================================================================
def isPrime(n: int) -> bool:
    if n == 0 or n == 1:
        return False
    for i in range(2, n + 1):
        if i * i > n: # √N以下まで見ればいい。i*iとして比較するのは小数を扱いたくないため。
            return True
        if n % i == 0:
            return False
# ======================================================================================
```

### 約数列挙

```python
# ----------------------------------------------------------------
# Input
#   1. 約数を求めたい数
# Output
#   約数リスト(昇順)
# Order
#   O(√n)
# ----------------------------------------------------------------
def getDivisors(n: int):
    lowerDivisors, upperDivisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lowerDivisors.append(i)
            if i != n // i:
                upperDivisors.append(n//i)
        i += 1
    return lowerDivisors + upperDivisors[::-1]
```

### 約数の個数

```python
def getNumOfDividors(n: int) -> int:
    numOfDividors = 1
    i = 2
    while i * i <= n:
        ex = 0
        while n % i == 0:
            ex += 1
            n //= i
        if ex != 0:
            numOfDividors *= ex + 1
        i += 1
    if n != 1:
        numOfDividors *= 2
    return numOfDividors
```

### 素因数分解

```python
# ----------------------------------------------------------------
# Input
#   1. 素因数を求めたい数
# Output
#   素因数(辞書)
# Order
#   O(√n)
# ----------------------------------------------------------------
def primeFactrization(n: int) -> dict:
    primeFactors = dict()
    i = 2
    while i * i <= n:
        ex = 0
        while n % i == 0:
            ex += 1
            n //= i
        if ex != 0:
            primeFactors[i] = ex
        i += 1
    if n != 1:
        primeFactors[n] = 1
    return primeFactors
```

```python
# ----------------------------------------------------------------
# Input
#   1. 素因数を求めたい数
# Output
#   素因数(昇順リスト)
# Order
#   O(√n)
# ----------------------------------------------------------------
def primeFactrization(n: int) -> list:
    primeFactors = list()
    i = 2
    while i * i <= n:
        while n % i == 0:
            primeFactors.append(i)
            n //= i
        i += 1
    if n != 1:
        primeFactors.append(n)
    return primeFactors
```


```python:while->for高速化
def primeFactrization(n: int) -> dict:
    primeFactors = dict()
    for i in range(2, n):
        if i * i > n:
            break
        ex = 0
        for _ in range(n):
            if n % i != 0:
                break
            ex += 1
            n //= i
        if ex != 0:
            primeFactors[i] = ex
    if n != 1:
        primeFactors[n] = 1
    return primeFactors
```

### 組み合わせ

```python
# ----------------------------------------------------------------
# Input
#   1,2: nCr
# Output
#   組み合わせの数
# Order
#   ??
# ----------------------------------------------------------------
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
 
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r + 1):                    # p番目について、
        pivot = denominator[p - 1]              # pivotで約分を試みる。
        if pivot > 1:                           # ただし、pivotが1、すなわちすでに割り尽くされているならp番目は飛ばす。
            offset = (n - r) % p
            for k in range(p-1,r,p):            # p番目を約分できるということはp番目からpの倍数番目も約分可能なので実施する。
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
 
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result
```

### modpow

```python
# n^a % MOD の算出
def modpow(n: int, a: int, mod: int = MOD) -> int:
    res = 1
    while a > 0:
        if a & 1:
            res = res * n % mod
        n = n * n % mod
        a >>= 1
    return res
# ======================================================================================
```

### 直交座標ー極座標 変換

```python
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
```

```python
def solve(N: int, K: int, a: "List[int]"):
    # [l, r) 右側は開区間。そのindexを含まない。
    r = 0
    l = 0
    ans = 0
    sum = 0
    for _ in range(N):
        while r < N and """rをインクリメントするために満たす条件""":
            # なんらかの処理
            # eg) sum += a[r]
            r += 1
        if """lをインクリメントするために満たす条件""":
            # なんらかの処理
            # ans += N - r + 1
            # sum -= a[l]
            l += 1
    print(ans)
```