## 隣接リスト作成

```python
N = 0 # 頂点数
M = 0 # 辺の数
a,b = [], [] # 連結した頂点。a-b
G = [[] for _ in range(N)]
for i in range(M):
    G[a[i] - 1].append(b[i] - 1)
    G[b[i] - 1].append(a[i] - 1)

print(G)

# 周囲を"#"などで囲う場合、 W + 2にすることに注意！
F = []
F.append("#" * (W + 2))
for _ in range(H):
    F.append("#" + input() + "#")
F.append("#" * (W + 2))
```


## インタラクティブな問題のバッファのフラッシュ

```python
sys.stdout.flush()
```


## 多重ループからのbreak
```python
for i in range(10):
    for j in range(10):
        if i == j * 2:
            break
    else: # for-elseでbreakしなかったら入ってくる。
        continue
    break
```

## 辞書のソート

sorted(d.items(), key=lambda x:x[0])

## 入力受け取り

```python
# 高速化
input = lambda: sys.stdin.readline().strip()
```

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

## 2次元配列回転
-> Math.py移動

## 区間スケジューリング
```python
# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b
l = [(bb, aa) for aa, bb in zip(A, B)]
l.sort()
now = 0
ans = 0
for bb, aa in l:
    if now < aa:
        now = bb
        ans += 1
print(ans)
return
```

### ビット全探索
-> BitFullSearch.py

### 累積和(DP算出)

```python
class MatrixAccumulates:
    def __init__(self, H: int, W: int) -> None:
        self.H, self.W = H, W
        self.LL = [[0] * W for _ in range(H)]
        self.S = []
    
    def add(self, y, x, val):
        self.LL[y][x] += val
        return

    def setList(self, LL: "List[List[int]]"):
        self.LL = LL
        return

    def build(self, index1: bool = False):
        if index1:
            self.S = [[0] * self.W for _ in range(self.H)]
            #ヨコに累積和
            for i in range(self.H):
                for j in range(self.W):
                    if i == 0:
                        self.S[i][j] = self.LL[i][j]
                    else:
                        self.S[i][j] = self.S[i-1][j] + self.LL[i][j]
            #タテに累積和
            for i in range(self.H):
                for j in range(self.W):
                    if j == 0:
                        self.S[i][j] = self.S[i][j]
                    else:
                        self.S[i][j] = self.S[i][j-1] + self.S[i][j]
        else:
            # 累積和(DPで算出)
            # 0行目/0列目に0を挿入した二次元累積和Sを得る。
            self.S = [[0] * (self.W + 1) for _ in range(self.H + 1)]
            for i in range(self.H):
                for j in range(self.W):
                    self.S[i + 1][j + 1] = self.S[i + 1][j] + self.S[i][j + 1] - self.S[i][j] + self.LL[i][j]
        return
    
    def getArea(self, excY, incY, excX, incX) -> int:
        '''
        exampl) excX = 1, excY = 0, incX = 3, incY = 2
                excX  incX
                0  1  2  3
        excY 0  x  x  x  x
             1  x  x  o  o
        incY 2  x  x  o  o
        '''
        areaAccumulate = self.S[incY][incX] - self.S[excY][incX] - self.S[incY][excX] + self.S[excY][excX]
        return areaAccumulate
    
    def printS(self) -> int:
        for i in range(self.H):
            print(self.S[i])
        return
```

### 累積和(ゼータ変換)

```python
# 二次元累積和
# 0行目/0列目に0を挿入しない累積和を得る。
def zetaConvert(l: "List[List[int]]"):
    H, W = len(l), len(l[0])
    #ヨコに累積和
    for i in range(H):
        for j in range(W):
            if i: l[i][j] += l[i-1][j]
    #タテに累積和
    for i in range(H):
        for j in range(W):
            if j: l[i][j] += l[i][j-1]
    return None

# 累積和
# 0行目/0列目に0を挿入する。
S = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        S[i+1][j+1] = S[i+1][j] + S[i][j+1] - S[i][j] + A[i][j]
```

### DFS

```python
sys.setrecursionlimit(10 ** 9)
class DFS():
    def __init__(self, G: "list[list[int]]", rG: "list[list[int]]"):
        self.nodesNum = len(G)                  # 頂点数
        self.G = G                              # グラフ
        self.rG = rG                            # 全ての辺を逆向きにしたグラフ
        self.seen = [False] * self.nodesNum     # 各ノードが訪問済みかどうかのフラグ
        self.firstOrder = []                    # ノードの行きがけ順(0-index)
        self.lastOrder = []                     # ノードの帰りがけ順(0-index)
        self.connections = [-1] * self.nodesNum # 強連結成分分解の結果
        self.sccNum = 0                         # 強連結成分の採番用カウンタ
    
    # DFS
    def dfs(self, now: int):
        self.firstOrder.append(now)
        self.seen[now] = True
        for next in self.G[now]:
            if self.seen[next]:
                continue
            self.dfs(next)
        self.lastOrder.append(now)
    
    # 逆向きグラフの強連結成分チェック
    def reverseDfs(self, now: int):
        self.seen[now] = True
        self.connections[now] = self.sccNum
        for next in self.rG[now]:
            if self.seen[next]:
                continue
            self.reverseDfs(next)
    
    # 強連結成分分解SCC
    def scc(self):
        # 帰りがけ順のナンバリングDFS
        for startNode in range(self.nodesNum):
            if self.seen[startNode]:
                continue
            self.dfs(startNode)
        # seenをリセット
        self.seen = [False] * N
        # 帰りがけ順の大きい方から順に強連結成分の判定DFS
        for node in self.lastOrder[::-1]:
            if self.seen[node]:
                continue
            self.reverseDfs(node)
            self.sccNum += 1
```

```python
# = dfs(グラフ) =======================================================================
# ----------------------------------------------------------------
# Input
#   1. 現在の値
# Output
#   O(N + M)
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

def dfs(now)

# = 行きがけ/帰りがけDFS =================================================================
sys.setrecursionlimit(10 ** 9)
seen = [False] * N
firstOrder = []
lastOrder = []
def dfs(nodes: "list[list[int]]", now: int):
    firstOrder.append(now)
    seen[now] = True
    for next in nodes[now]:
        if seen[next]:
            continue
        dfs(nodes, next)
    lastOrder.append(now)
dfs(nodes, 0)
print("No,", "go", "back")
for i in range(N):
    print(i + 1, firstOrder[i] + 1, lastOrder[i] + 1)



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

# = dfs(グリッド) =======================================================================
H, W = map(int, input().split())
field = []
seen = []
for _ in range(H):
    field.append(input())
    seen.append([False] * W)
sys.setrecursionlimit(10 ** 9)
def dfs(y, x):
    seen[y][x] = True
    # 次の探索(分岐)
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_y = y + dy
        next_x = x + dx
        # 探索しない条件を切り落とし
        if next_x < 0 or next_y < 0 or next_x >= W or next_y >= H or field[next_y][next_x] == "#" or seen[next_y][next_x]:
            continue
        dfs(next_y, next_x)
    return
```

### 桁DP テンプレート

```python
L = len(S)
dp = [[[0] * D for _ in range(2)] for _ in range(L + 1)]
dp[0][0][0] = 1

for i in range(1, L + 1):
    for smaller in range(2):
        for j in range(D):      # jの範囲や遷移先の式は問題毎に書き換え
            maxNum = int(N[i - 1]) if smaller == 0 else 9
            for num in range(maxNum + 1):
                dp[i][smaller or num < int(N[i - 1])][(j + num) % D] += dp[i - 1][smaller][j]
                dp[i][smaller or num < int(N[i - 1])][(j + num) % D] %= MOD
print((dp[-1][0][0] + dp[-1][1][0] + MOD - 1) % MOD)
```


### SCC

```python
sys.setrecursionlimit(10 ** 9)
class SCC():
    def __init__(self, nodesNum: int):
        self.nodesNum = nodesNum                            # 頂点数
        self.G = [[] for _ in range(self.nodesNum)]         # グラフ
        self.rG = [[] for _ in range(self.nodesNum)]        # 全ての辺を逆向きにしたグラフ
        self.seen = [False] * self.nodesNum                 # 各ノードが訪問済みかどうかのフラグ
        self.lastOrder = []                                 # ノードの帰りがけ順(0-indexで採番)
        self.tplCorrespondenceTable = [-1] * self.nodesNum  # SCC後の対応表(indexがノード番号。値が0-indexで採番された順番。値が若いものから順にトポロジカルソートされている)
        # self.topologicalSortedList = []                     # SCC後のトポロジカルソート済みリスト
        self.sccNum = 0                                     # 強連結成分の採番用カウンタ(0-indexで採番)
    
    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int):
        self.G[fromNode].append(toNode)
        self.rG[toNode].append(fromNode)

    # DFS
    def _dfs(self, now: int):
        self.seen[now] = True
        for next in self.G[now]:
            if self.seen[next]:
                continue
            self._dfs(next)
        self.lastOrder.append(now)
    
    # 逆向きグラフの強連結成分チェック
    def _reverseDfs(self, now: int):
        self.seen[now] = True
        self.tplCorrespondenceTable[now] = self.sccNum
        # self.topologicalSortedList.append(now)
        for next in self.rG[now]:
            if self.seen[next]:
                continue
            self._reverseDfs(next)
    
    # 強連結成分分解SCC
    def scc(self):
        # 帰りがけ順のナンバリングDFS
        for startNode in range(self.nodesNum):
            if self.seen[startNode]:
                continue
            self._dfs(startNode)
        # seenをリセット
        self.seen = [False] * self.nodesNum
        # 帰りがけ順の大きい方から順に強連結成分の判定DFS
        for node in self.lastOrder[::-1]:
            if self.seen[node]:
                continue
            self._reverseDfs(node)
            self.sccNum += 1
        return self.tplCorrespondenceTable
    
    # 2つのノードが強連結か。
    def same(self, a: int, b: int):
        return self.tplCorrespondenceTable[a] == self.tplCorrespondenceTable[b]

# usage
d = SCC(N) # グラフ生成
for i in range(M):
    d.addEdge(a[i], b[i]) # 辺の追加
cmp = d.scc() # 強連結成分分解
# トポロジカルソート済みのリストが欲しい場合はd.topologicalSortedListを利用する。
```

## 動的計画法

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

### 組み合わせ -> 移植済み

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
# 
# abc065_c
# ----------------------------------------------------------------
MAX = 666667      # Pythonだと7.3 * 10^5程度が限度。それ以上はTLE(>2s)
# MAX = 10 ** 6   # Pypyで 260~280 msくらい
MOD = 1000000007  # type: int

fac, finv, inv = [1, 1], [1, 1], [0, 1]
# fac : 階乗(1,2,6,...)
# inv : 逆元(1,2,...N) -> inv[i] = pow(i, 10 ** 9 + 5, 10 ** 9 + 7)
# finv: 逆元(階乗の逆元 = 1!の逆元, 2!の逆元, 3!の逆元)
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
    print(cmbMod(100, 50))
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
        # print("#", l, r, sum)
        sum += a[r]
        r += 1
    if "左端を進め、範囲を狭める条件":
        # print(">", l, r, sum)
        ans += N - r + 1
        sum -= a[l]
        l += 1
```



```python

def max2D(LL: "List[List[int]]", init: int = 0):
    res = init
    for i in range(len(LL)):
        print(LL[i])
        res = max(res, max(LL[i]))
    return res
```

## 最下位ビットの取り出し

```python
for p in range(20):
    print(bin(p))
    print(p, ":", p&-p) # 最下位ビットを取り出し
```