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

## 二次元配列

```python
arr = [[0] * W for _ in range(H)]
# def generate2Darray(height: int, width: int, init: int) -> "List[List[int]]":
#     res = []
#     for _ in range(height):
#        res.append([init] * width)
#     return res
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
        if is_ok(mid):
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
def bfs(edges: "List[to]", start_node: int) -> list:
    q = set()
    dist = [INF] * len(edges)
    q.add(start_node)
    dist[start_node] = 0
    while len(q) != 0:
        now = q.pop()
        for next in edges[now]:
            if dist[next] != INF:
                continue
            q.add(next)
            dist[next] = dist[now] + 1
    return dist



# 未検証 deprecated
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

def dfs(edges: "List[to]", start_node: int) -> list:
    s = []
    dist = [INF] * len(edges)
    dist[start_node] = 0
    s.append(start_node)
    while not len(s) == 0:
        now = s.pop()
        for next in edges[now]:
            if dist[next] != INF:
                continue
            s.append(next)
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