## 隣接リスト作成

```python
N = 0 # 頂点数
M = 0 # 辺の数
a,b = [], [] # 連結した頂点。a-b
nodes = [[] for _ in range(N)]
for i in range(M):
    nodes[a[i] - 1].append(b[i] - 1)
    nodes[b[i] - 1].append(a[i] - 1)

print(nodes)
```

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

## 外部モジュール

```python
import string
# https://docs.python.org/ja/3/library/string.html
print(string.ascii_lowercase)
# >> abcdefghijklmnopqrstuvwxyz
```

## ランレングス圧縮

```python
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] 
def runLengthEncode(S: str) -> "List[tuple(str, int)]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

# RUN LENGTH DECODING list(tuple()) -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L: "list[tuple]") -> str:
    res = ""
    for c, n in L:
        res += c * int(n)
    return res

# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1" 
def runLengthEncodeToString(S: str) -> str:
    grouped = groupby(S)
    res = ""
    for k, v in grouped:
        res += k + str(len(list(v)))
    return res
```

### 座標圧縮

```python
L = []
d = {val : i + 1 for i, val in enumerate(sorted(list(set(L))))}
```

## 探索

### 二分探索

```python
# True ------ ok | ng ---- False
def is_ok(k: int):
    return k * (k + 1) // 2 <= n + 1    # 条件式

def binSearch(ok: int, ng: int):
    # print(ok, ng)              # はじめの2値の状態
    while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
        mid = (ok + ng) // 2
        # print("target > ", mid)
        result = is_ok(mid)
        # print(result)
        if result:
            ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
        else:
            ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
        # print(ok, ng)          # 半分に切り分ける毎の2値の状態
    return ok        
```

### ビット全探索

```python
# 2^N 通りのビット全探索。
for n in range(2 ** N):
    for i in range(N):
        if (n >> i) & 1:
            # i桁目のビットが立っている場合の処理
            pass
```

### DFS

```python
# = dfs(グラフ) =======================================================================
# ----------------------------------------------------------------
# Input
#   1. 隣接リスト
#   2. 開始ノード
# Output
#   スタートから各ノードへの最小コスト
# Order
# 
# ----------------------------------------------------------------
sys.setrecursionlimit(10 ** 9)
def dfs(now: int):
    res = 0
    nums = [3, 5, 7]
    # --- 探索終了条件 ----------------------------
    if now > N:
        return res
    # --- カウントアップ条件 -----------------------
    S = str(now)
    check = True
    for i in nums:
        if not str(i) in S:
            check = False
    if check:
        res += 1
    # --- 次の探索(分岐) --------------------------
    for num in nums:
        next = now * 10 + num
        res += dfs(next)
    return res

# = オイラーツアー =======================================================================
# https://atcoder.jp/contests/abc213/submissions/24899201
# https://hcpc-hokudai.github.io/archive/graph_tree_001.pdf

# 頂点
eularTourNodes = []
sys.setrecursionlimit(10 ** 9)
def getEularTourNodes(now: int, pre: int = -1):
    eularTourNodes.append(now)
    for next in nodes[now]:
        if next == pre:
            continue
        getEularTourNodes(next, now)
        eularTourNodes.append(now)
    return
getEularTourNodes(0)

# 辺
eularTourEdges = []
sys.setrecursionlimit(10 ** 9)
def getEularTourEdges(now: int, pre: int = -1):
    eularTourEdges.append(now)
    for next in nodes[now]:
        if next == pre:
            continue
        getEularTourEdges(next, now)
    eularTourEdges.append(-now)
    return
```

### BFS

```python
# = bfs(グラフ) =======================================================================
# ----------------------------------------------------------------
# Input
#   1. 隣接リスト
#   2. 開始ノード
# Output
#   スタートから各ノードへの最小コスト
# Order
# 
# ----------------------------------------------------------------
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
# = bfs(グリッド) =======================================================================
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
from collections import deque
def bfs(edge, H, W, startX, startY) -> list:
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
# ======================================================================================
```

## 動的計画法

### dijkstra / ダイクストラ

```python
# = dijkstra ===========================================================================
# ----------------------------------------------------------------
# Input
#   1. タプル(重み, 行先)の二次元配列(隣接リスト)
#   2. 探索開始ノード(番号)
# Output
#   スタートから各ノードへの最小コスト
# Order
#   O((V + E) * logV)
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
#   最長共通部分列
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

### エラトステネスの篩

ある数limitまでの素数を列挙。

```python
# ======================================================================================
# Order
# O(NloglogN)
# ======================================================================================
def getPrimeLists(limit: int):
    primes = [] # 素数リスト
    isPrime = [True] * (limit + 1) # 素数かどうかのフラグ
    isPrime[0] = False
    isPrime[1] = False
    
    for p in range(limit + 1):  # p : 判定対象の数
        if not isPrime[p]:
            continue
        primes.append(p)
        # pが素数のためそれ以降に出現するpの倍数を除外する。
        # なお、ループはp始まりでも良いが、p * _ のかける側はすでに同じ処理で弾かれているはずのため無駄。
        for i in range(p * p, limit + 1, p):
            isPrime[i] = False
    return primes

# 発展形 : limitまでの数の素数の個数列挙
def getNumOfPrime(limit: int):
    numOfPrime = [0] * (limit + 1) # ある数の素因数の個数
    numOfPrime[0] = 0
    numOfPrime[1] = 0

    for p in range(2, limit + 1): # p : 判定対象の数
        # pが素数の場合、pの倍数の数にpが素因数となるのでインクリメント
        if not numOfPrime[p]:
            for i in range(p, limit + 1, p):
                numOfPrime[i] += 1
    return numOfPrime
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
# 階乗の逆元の前処理をしてMODとる場合は->modinvへ
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
# 二分累乗法
MOD = 10 ** 9 + 7
def modpow(n: int, a: int, mod: int = MOD) -> int:
    res = 1
    while a > 0:
        if a & 1:
            res = res * n % mod
        n = n * n % mod
        a >>= 1
    return res
```

### modinv

```python
# ----------------------------------------------------------------
# Input
#   1,2: nCr % mod
# Output
#   組み合わせの数
# Order
#   ??
# Note:
#   MAX定数にnCkのn+1の値を入れる。種々のリスト作成される。
#   初めにcmbInit()を呼び、階乗、階乗の逆元のリストを算出する。
# ----------------------------------------------------------------
MAX = 666667      # Pythonだと7.3 * 10^5程度が限度。それ以上はTLE(>2s)
# MAX = 10 ** 6   # Pypyで 260~280 msくらい
MOD = 1000000007  # type: int

fac, finv, inv = [1, 1], [1, 1], [0, 1]
# fac : 階乗(1,2,6,...)
# inv : 逆元(1,2,...N) -> inv[i] = pow(i, 10 ** 9 + 5, 10 ** 9 + 7)
# finv: 逆元(階乗の逆元 = 1の逆元, 2の逆元, 6の逆元)
def cmbInit():
    for i in range(2, MAX):
        fac.append(fac[i - 1] * i % MOD)
        inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
        finv.append(finv[i - 1] * inv[i] % MOD)

# 二項係数計算
def cmbMod(n: int,k: int):
    if n < k: return 0
    if n < 0 or k < 0: return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

# Usage
def solve():
    cmbInit()
    print(cmb(100, 50))
    return
```

### ダブリング

```python
class Doubling:
    def __init__(self, stateKind: int, maxDoublingTimes: int):
        self.dv = []                                # dv[k][s] := 状態sを2^k回実行したらあとの状態
        self.stateKind = stateKind                  # 状態の種類数s
        self.maxDoublingTimes = maxDoublingTimes    # 実行回数kの範囲の定義(2^0 ≦ k ≦ 2^maxDoublingTimes)
        self.initTable()
        self.createTable()
    
    # 初期化処理
    def initTable(self):
        self.dv.append(A) 
    
    def createTable(self):
        for i in range(1, self.maxDoublingTimes):
            l = []
            for j in range(self.stateKind):
                l.append(self.dv[i - 1][self.dv[i - 1][j]])
            self.dv.append(l)
        
    def getState(self, doubingTimes: int, startState: int):
        a = []
        for i in range(self.maxDoublingTimes):
            if doubingTimes >> i & 1:
                a.append(i)
        now = startState
        for i in a:
            now = self.dv[i][now]
        return now
    def getAllStates(self, targenTime: int):
        return self.dv[targenTime]

import math
d = Doubling(N, int(math.log2(K)) + 1)
print(d.getState(K, 0))
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

リスト内の一致する要素を全て取り出す。
```python
def findSome(l: "List", val: any):
    return [i for i, x in enumerate(l) if x == val]
```


```python
# 遅い deprecated
import queue
def bfs(edges: "List[to]", start_node: int) -> list:
    # deprecated
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
```


### Union-Find木

```python
from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
```

### 尺取り法

```python
# リストa (要素数N)

# a[l:r]を考える。rはこの範囲に含まれない。
# 例) a[0:3] → a[0]〜a[2]までの範囲
l = 0
r = 0
ans = 0
sum = 0
for _ in range(N):
    while r < N and "右端を進め、範囲を広げる条件":
        sum += a[r]
        r += 1
    if "左端を進め、範囲を狭める条件":
        ans += N - r + 1
        sum -= a[l]
        l += 1
```

### N進数変換

```python
# from N進数 to 10進数
int(baseNvalue ,n) # 2,8,16のみ

# from 10進数 to N進数
def base10int(base10value, toBase):
    ans = []
    p = base10value
    while p >= toBase:
        p, q = divmod(p, toBase)
        ans.append(str(q))
    ans.append(str(p))
    return "".join(ans[::-1])
```