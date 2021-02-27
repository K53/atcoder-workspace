# 入力受け取り

## マス目

```txt
H W
...
.#.
.#.
```

```python
# -----------------------------
# 方法1)
#   値の書き換えが発生しない場合
# -----------------------------
H, W = map(int, input().split())
l = []
for _ in range(H):
    l.append(input())
print(l)
# ['.....', '.###.', '.###.', '.###.', '.....']
print(l[0][0])
# .
l[0][0] = "a"   # 置き換え不可

# -----------------------------
# 方法1)
#   値の書き換えをする場合
# -----------------------------
H, W = map(int, input().split())
l = []
for _ in range(H):
    l.append(list(input()))
print(l)
# [['.', '.', '.', '.', '.'], ['.', '#', '#', '#', '.'], ['.', '#', '#', '#', '.'], ['.', '#', '#', '#', '.'], ['.', '.', '.', '.', '.']]
print(l[0][0])
# .
l[0][0] = "a"   # 置き換え可能
```


# 順列 / 組み合わせ系

## 順列 P

### 順列の全列挙

```python
import itertools

l = ['a', 'b', 'c', 'd']

p = itertools.permutations(l, 2) # 第二引数は選択する要素数。
# 型： <class 'itertools.permutations'>

for v in itertools.permutations(l, 2):
    print(v)
# ('a', 'b')    # タプル
# ('a', 'c')
    ・
    ・
    ・
```

https://note.nkmk.me/python-math-factorial-permutations-combinations/

### 順列の個数

```python
# ToDo
```

## 組み合わせ C

### 組み合わせの全列挙

```python
import itertools

l = ['a', 'b', 'c', 'd']

p = itertools.combinations(l, 2) # 第二引数は選択する要素数。
# 型： <class 'itertools.combinations'>

for v in itertools.combinations(l, 2):
    print(v)
# ('a', 'b')    # タプル
# ('a', 'c')
    ・
    ・
    ・
```

### 組み合わせの個数

```python
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
            for k in range(p-1,r,p):            # p番目を約分できるということはp番目からpの倍数番目も約分可能なので実施する。
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
```

# ビット/n進数系

## n進数変換

```python:n進数に変換する標準関数
bin() # 2進数表記の文字列に変換
oct() # 8進数表記の文字列に変換
hex() # 16進数表記の文字列に変換

# 逆に文字列表記のn進数を10進数の数字に戻す時はintの第二引数に基数を指定する。

int("10", 8) # 8進数表記の"10"を10進数の数字に変換。
```

## 2択をN回繰り返す全探索

N択からどちらか1つを選ぶ行為をK回行う組み合わせ → N^K通り

1) N^Kが実行時間的に許容範囲である。  → 全探索。
2) N = 2。  → ビット演算を用いて高速に計算可能。

```python
for i in range(2 ** K):     # 2^K通り全探索
    for b in range(K):      # ビットを1つずつずらしていく
        if (i >> b) & 1:    # その都度、最下位ビットが立っているかを見る。
            # bitが立っている = b番目が選択されている時の処理
        else:
            # bitが立っていない = b番目を選択していない時の処理
```

## 他

```python
L = [99, 98, 97]
for i, val in enumerate(L, 10):
    print(i, val)
    # 10 99
    # 11 98
    # 12 97
```

## ビット反転

### 1) ビットを反転させる。

x = 0なら1に、x = 1なら0にしたい時。
単純に反転させる`~`は使用できないことに注意。

#### ~ (ビット反転)

`~x` = `-(x + 1)`となる。これはxを2の補数形式とみなして反転した結果が返るため。

#### ^ (排他的論理和 XOR)

```
0 ^ 0 = 0
1 ^ 0 = 0
0 ^ 1 = 1
1 ^ 1 = 0
```

0は影響を与えず、1はビットを反転させることからビットを反転させるには`x ^ 1`

### 2) 特定のビットを反転させる。

N桁のビット列のうち特定のk番目のビットのみを反転させたい時、ビットシフトと組み合わせて`x ^ (1 << k)`で実現できる。

https://yottagin.com/?p=5261

# 2つのデータ構造の共通要素

2つの集合の共通要素を取得する。

```python
A = set()
B = set()
common = A & B      # 共通要素の集合
diff = A ^ B    # 共通でない要素の集合
```

https://note.nkmk.me/python-list-common/


リスト内の要素の重複を調べるツール`collections.Counter()`を用いることで何がいくつ重複しているかの辞書のサブクラスである`collections.Counter`として得られる。

```python
import collections

l = [3, 3, 2, 1, 5, 1, 4, 2, 3]

print(collections.Counter(l))
# Counter({3: 3, 2: 2, 1: 2, 5: 1, 4: 1})
```

# 約数

検証問題
https://atcoder.jp/contests/abc180/tasks/abc180_c

```
# 約数列挙
def getDivisors(n: int):
    # validation check
    if not isinstance(n, int):
        raise("[ERROR] parameter must be integer")
    if n < 0:
        raise("[ERROR] parameter must be not less than 0 (n >= 0)")

    lowerDivisors, upperDivisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lowerDivisors.append(i)
            if i != n // i:
                upperDivisors.append(n//i)
        i += 1
    return lowerDivisors + upperDivisors[::-1]

# 約数列挙
N = 120
print(getDivisors(N))
# [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]
```

# 部分列列挙

```python
# 文字列Tに含まれる部分列を全列挙する。(重複要素排除なしのため未完成)
t = len(T)
for l in range(t):
    for r in range(0, t - l):
        c = T[l:(t - r)]
        print(c)
```

------------------------------------------------------------------------------------------------------------------------------------------------

* edgeにコストなし(コストが全て等価)
    - 幅優先探索 BFS
        - 最短経路
        - マップ上の最長距離算出
    - 深さ優先探索 DFS
        - 到達可否
        - 経路カウント
* edgeのコストあり
    - ダイクストラ法


# 幅優先探索 BFS

## 迷路の最短距離

理論/理解
https://qiita.com/drken/items/996d80bcae64649a6580

問題
https://atcoder.jp/contests/atc002/tasks/abc007_3

```python
# [Input]
# 7 8
# 2 2
# 4 5
# ########
# #......#
# #.######
# #..#...#
# #..##..#
# ##.....#
# ########
q = queue.Queue()
H, W = map(int, input().split())
sy, sx = map(lambda n: int(n) - 1, input().split())
gy, gx = map(lambda n: int(n) - 1, input().split())
field = []
dist = []                                        # スタートから何歩で移動できるか(数値) 兼 既に訪問したか(-1 or not)
for _ in range(H):
    field.append(input())
    dist.append([-1] * W)
q.put((sx, sy))
dist[sy][sx] = 0
while not q.empty():
    x, y = q.get()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + dx, y + dy
        if field[next_y][next_x] == "#" or dist[next_y][next_x] != -1:
            continue
        q.put((next_x, next_y))
        dist[next_y][next_x] = dist[y][x] + 1
print(dist[gy][gx])
```

## マップ上の最長距離

問題
https://atcoder.jp/contests/abc151/tasks/abc151_d

```python
    q = queue.Queue()
    H, W = map(int, input().split())
    field = [input() for _ in range(H)]
    dist = []
    ans = -1
    for sy in range(H):
        for sx in range(W):
            if field[sy][sx] == "#":
                continue
            dist = [[-1] * W for _ in range(H)]
            q.put((sx, sy))
            dist[sy][sx] = 0
            while not q.empty():
                x, y = q.get()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    next_x, next_y = x + dx, y + dy
                    if 0 <= next_x < W and 0 <= next_y < H and field[next_y][next_x] != "#" and dist[next_y][next_x] == -1:                        
                        q.put((next_x, next_y))
                        dist[next_y][next_x] = dist[y][x] + 1
            for d in dist:
                ans = max(ans, max(d))
    print(ans)
```

## テンプレート

```
# 作成と初期化
## リスト(1)作成   -> フィールドを表す2次元リストを生成 (入力から受け取る)
## キュー作成      -> [訪問する予定の場所の順番]用 (スタート地点をエンキュー)
## リスト(2)作成   -> [最短歩数]兼[訪問済みかのフラグ]用2次元リスト (スタート地点のみ0、他は-1で初期化)

# 探索 (以下をキューが空になるまで繰り返す)
## キューから取り出し
### 移動可能な隣接4マスのチェック (これらを満たさない場合はskip)
###   * そこは壁(制約上到達不能な箇所)でないこと
###   * 未訪問(リスト2の値が初期値-1)であること
### キューに移動先をエンキュー
### リスト2にそこまでかかる歩数を書き込み(現在のマスの到達歩数+1を代入)
```

同じくBFSはグラフの場合にも適応可能。
https://atcoder.jp/contests/abc161/tasks/abc161_d
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=ja

単純に`移動可能な隣接4マス`を`その頂点から辺を辿って移動可能な頂点`に変えて実施すればよい。
そのため迷路問題ではリスト1はフィールドそのものを示していたが、今回は`ある頂点から辺を辿って移動可能な頂点のリスト`を入れておくことが必要となる。

# 深さ優先探索 DFS

理論/理解
https://qiita.com/drken/items/a803d4fc4a727e02f7ba

解法はスタックと再帰の2つ

* スタック → BFSのキューをスタックに置き換えたらいい。単純な到達可否なら○
* 再帰関数 → 経路や条件を満たす個数のカウントが必要になる場合こっちの方が楽。スタックだと分岐毎にスタックを生成する必要がある気がする。

## 迷路の到達可否
問題
https://atcoder.jp/contests/atc001/tasks/dfs_a

```python:スタックver.
# [Input]
# 4 5
# s####
# ....#
# #####
# #...g
stack = []
H, W = map(int, input().split())
field = []
dist = []  
field.append("#" * (W + 2))
dist.append([-1] * (W + 2))
for _ in range(H):
    field.append("#" + input() + "#")
    dist.append([-1] * (W + 2))
field.append("#" * (W + 2))
dist.append([-1] * (W + 2))

for h in range(1, H + 1):
    for w in range(1, W + 1):
        if field[h][w] == "s":
            stack.append((w, h))     #x, y

while len(stack) > 0:
    target_x, target_y = stack[0]
    stack = stack[1:]
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = target_x + dx, target_y + dy
        if field[next_y][next_x] == "g":
            print(YES)
            return
        if field[next_y][next_x] == "#" or dist[next_y][next_x] != -1:
            continue
        stack.append((next_x, next_y))
        dist[next_y][next_x] = dist[target_y][target_x] + 1
print(NO)
return
```

```python:再帰関数ver(再起呼び出し前にdist評価)
#!/usr/bin/env python3
import sys
sys.setrecursionlimit(500 * 500)

YES = "Yes"  # type: str
NO = "No"  # type: str

H, W = 0, 0
field = []
dist = []  

def dfs(x, y):
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < W and 0 <= next_y < H and field[next_y][next_x] != "#" and dist[next_y][next_x] == -1:
            dist[next_y][next_x] = dist[y][x] + 1
            if field[next_y][next_x] == "g"or dfs(next_x, next_y):
                return True
    return False

def main():
    global H, W
    H, W = map(int, input().split())
    for _ in range(H):
        field.append(input())
        dist.append([-1] * W)

    for h in range(H):
        for w in range(W):
            if field[h][w] == "s":
                dist[h][w] = 0
                print(YES if dfs(w, h) else NO)
                return

if __name__ == '__main__':
    main()

```

```python:再帰関数ver(再起呼び出し先でdist評価)
#!/usr/bin/env python3
import sys
sys.setrecursionlimit(500 * 500)

YES = "Yes"  # type: str
NO = "No"  # type: str

H, W = 0, 0
field = []
dist = []  

def dfs(x, y, d):
    dist[y][x] = d
    if field[y][x] == "g":
        return True
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < W and 0 <= next_y < H and field[next_y][next_x] != "#" and dist[next_y][next_x] == -1:
            if dfs(next_x, next_y, d + 1):
                return True
    return False

def main():
    global H, W
    H, W = map(int, input().split())
    for _ in range(H):
        field.append(input())
        dist.append([-1] * W)

    for h in range(H):
        for w in range(W):
            if field[h][w] == "s":
                print(YES if dfs(w, h, 0) else NO)
                return

if __name__ == '__main__':
    main()

```

## テンプレート

```:スタックver
# 作成と初期化
## リスト(1)作成             -> フィールドを表す2次元リストを生成 (入力から受け取る)
## スタック(実質リスト)作成    -> [訪問する予定の場所の順番]用 (スタート地点をpush)
## リスト(2)作成             -> [最短歩数]兼[訪問済みかのフラグ]用2次元リスト (スタート地点のみ0、他は-1で初期化)

# 探索 (以下をゴールに到達するまで繰り返す)
## スタックからpop
### 移動可能な隣接4マスのチェック (これらを満たさない場合はskip)
###   * そこは壁(制約上到達不能な箇所)でないこと
###   * 未訪問(リスト2の値が初期値-1)であること
### スタックに移動先をappend
### リスト2にそこまでかかる歩数を書き込み(現在のマスの到達歩数+1を代入)
```

```:再帰関数ver
# 作成と初期化
## リスト(1)作成             -> フィールドを表す2次元リストを生成 (入力から受け取る)
## リスト(2)作成             -> [最短歩数]兼[訪問済みかのフラグ]用2次元リスト (スタート地点のみ0、他は-1で初期化)

# 再帰関数を定義              -> 再帰関数では引数で受け取るマスを評価する。
### 移動可能な隣接4マスのチェック (これらを満たさない場合はskip)
###   * そこは壁(制約上到達不能な箇所)でないこと
###   * 未訪問(リスト2の値が初期値-1)であること
### リスト2の対象のマスにそこまでかかる歩数を書き込み(現在のマスの到達歩数+1を代入)
### 終了条件の確認 return True
### 再帰関数呼び出し。
### 返り値がTrueならreturn True / そうでないならfor文続行
## retrun False             -> 4方位とも終了条件に引っかからなかったのでFalse
```

* 評価した結果visitedのフラグないしは歩数を書き込むのはキュー/再帰関数に渡す前後どちらでも構わない。(再帰は引数のマスを評価すると定義するなら呼び出し先で評価する方が正かもしれないが引数が増える)
* Pythonでは再起呼び出しに上限があるので評価対象のマスの数だけ上限を押し上げる必要あり(default上限は1000とかなのでランタイムエラーになる)

## その他のDFS

### 条件を満たす経路のカウント

カウントするケースはスタックだと面倒な気がする。

問題
https://atcoder.jp/contests/abc054/tasks/abc054_c

```python
# 3 3   頂点数 / 辺数(辺の情報は以下)
# 1 2
# 1 3
# 2 3
N, M = 0, 0
edge = []

# -------------------------------------------
# Parameters
#      visited : 訪問済みリスト(0/1)
#      s       : 訪問する頂点
# -------------------------------------------
def dfs(visited: "List[int]", s: int):
    count = 0
    for i in edge[s]:           # その頂点sに繋がる頂点全てについて到達可能な場所を調べる。
        if sum(visited) == N:
            return 1            # そのルートが条件を満たすので1つカウント
        if not visited[i]:      # 未到達なら"新しくvisitedリストを生成してdfsに渡す。
            count += dfs(visited[:i] + [1] + visited[i + 1:], i)  # stackでやろうとするとこの分岐の都度スタックと訪問済みフラグを生成する必要があってわけわかんなくなる。
    return count

N, M = map(int, input().split())
visited = [0] * N               # 訪問済みフラグ(0/1)
edge = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    edge[a - 1].append(b - 1)
    edge[b - 1].append(a - 1)

visited[0] = 1
ans = dfs(visited, 0)
print(ans)
return
```

### 島の数のカウント

visitedフラグが不要なタイプ。マップをそのまま変更(把握した島は海に沈めてやればいい)

問題1
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0067

```python
N = 12
field = []

def dfs(x, y):
    field[y][x] = 0     # 訪問済みの陸は沈める。
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < 12 and 0 <= next_y < 12 and field[next_y][next_x] == "1":
            dfs(next_x, next_y)
    return

def main():
    while True:
        ans = 0
        field.clear()
        for _ in range(N):
            field.append(list(str(input())))
        for y in range(N):
            for x in range(N):
                if field[y][x] == "1":
                    dfs(x, y)
                    ans += 1
        print(ans)
        try:
            input()
        except EOFError:
            break
    return
```

問題2
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=1160&lang=jp

```python
H, W = 0, 0
field = []

def dfs(x, y):
    field[y][x] = 0     # 訪問済みの陸は沈める。
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
        next_x, next_y = x + dx, y + dy
        if 0 <= next_x < W and 0 <= next_y < H and field[next_y][next_x] == "1":
            dfs(next_x, next_y)
    return

def main():
    while True:
        global H, W
        W, H = map(int, input().split())
        if W == H == 0:
            break
        ans = 0
        field.clear()
        for _ in range(H):
            field.append(input().split())
        for y in range(H):
            for x in range(W):
                if field[y][x] == "1":
                    dfs(x, y)
                    ans += 1
        print(ans)  
    return
```

### 数字の組み合わせ

4方位のチェックではなくその数字を選択した場合/しなかた場合の2択でDFS再帰呼び出し。

問題
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0030

```python
def dfs(target, capacity, sum):
    if capacity == 0 and sum == 0:
        return 1    # カウント1してreturn
    if target >= 10 or capacity < 0 or sum < 0:
        return 0
    # これまで4方位確認していたのが数字iをとるとらないの2択を確認している違いだけ。やってることは一緒
    return dfs(target + 1, capacity - 1, sum - target) + dfs(target + 1, capacity, sum) # 選択した場合 + 選択しない場合

def main():
    while True:
        n, s = map(int, input().split())
        if n == s == 0:
            break
        count = dfs(0, n, s)
        print(count)
    return
```

# ダイクストラ法

幅優先探索ではキューを用いたところを優先度付キュー(heapq)を用いた高速化version。
考え方はこの記事がとてもよくわかる。
https://qiita.com/zk_phi/items/d93f670544e4b9816ed0
結局、辺に重みがあってもその分勝手に一本道の頂点を増やして全ての辺の重みを1に揃えてあげれば幅優先探索が使えるので、重み付きでも考え方は大きく変わらない。
BFSで頑張ってもいいが、重み次第では時間がかかるので一本道を一気に進める様にヒープを用いたダイクストラ法を使って解くといった具合。

## 重み付の最短経路

問題
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A&lang=ja

```python:
#!/usr/bin/env python3
import heapq
INF = 10 ** 9
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

def main():
    V, E, r = map(int, input().split())
    edge = [[] for _ in range(V)]
    costs = []
    for _ in range(E):
        s, t, d = map(int, input().split())
        edge[s].append((d, t))

    dist = dijkstra(edge, r)

    for c in dist:
        print("INF" if c == INF else c)

if __name__ == '__main__':
    main()
```

問題
https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f

```python
import heapq
INF = 10 ** 9
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

def main():
    n, k = map(int, input().split())
    edge = [[] for _ in range(n)]
    for _ in range(k):
        i = list(map(int, input().split()))
        if i[0] == 1:
            edge[i[1] - 1].append((i[3], i[2] - 1))
            edge[i[2] - 1].append((i[3], i[1] - 1))
        else:
            costs = dijkstra(edge ,i[1] - 1)
            print(-1 if costs[i[2] - 1] == INF else costs[i[2] - 1])
    return
    
if __name__ == '__main__':
    main()
```

## テンプレート

BSFとほぼ変わらない。

```
# 作成と初期化
## リスト(1)作成   -> フィールドを表す2次元リストを生成 (入力から受け取る)
## キュー作成      -> [訪問する予定の場所の順番]用 (スタート地点をエンキュー)
## リスト(2)作成   -> [コスト]用 初期値はスタート地点のみ0、それ以外はINF

# 探索 (以下をキューが空になるまで繰り返す)
## キューから取り出し
## 既にその頂点により少ないコストで移動できるとわかっているならcontinue
### 移動可能な頂点のチェック (これを満たさない場合はskip)
###   * そこにいくことで最小コストを更新できること。(リスト2)
### キューに移動先をエンキュー
### リスト2にそこまでかかるコストを書き込み(現在のマスの到達歩数+移動コストを代入)
```

## 計算量

heapqの出し入れ : 1件につきlog(n)
→ popは頂点分で最大n回、pushは辺の分で最大e回なのでO((n+e)logn)
このため、e= n^2の完全グラフでは効率が悪くなる。

https://www-ui.is.s.u-tokyo.ac.jp/~takeo/course/2007/algorithm/dijkstra.pdf
https://www.ioi-jp.org/joi/2007/2008-yo-prob_and_sol/2008-yo-t6/review/2008-yo-t6-review.html

## 応用

### 往復するケース

問題
https://atcoder.jp/contests/abc035/submissions/20218577

有向グラフにおいて往復する場合、以下2つを求める必要がある。
* 始点1 → 経由地i
* 経由地i → 終点1
前者は問題ないが、後者に関して、全ての経由地iについてダイクストラをすると計算量が膨大になる。
その場合、各辺の向きを逆にして始点からダイクストラを行うことで経由地iからの帰りの経路を出すことができる。

```python
import heapq
INF = 10 ** 9
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
    N, M = map(int, input().split())
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges[a - 1].append((c, b - 1))
        edges[b - 1].append((c, a - 1))
    ans = INF
    for start in range(N):
        dist = dijkstra(edges, start)
        # print(dist)
        ans = min(max(dist), ans)
    print(ans)

if __name__ == '__main__':
    main()
```

### 多始点ダイクストラ

問題
https://atcoder.jp/contests/abc191/tasks/abc191_e
同じく往復する問題で、始点に自己ループとなる経路がある場合、
* 始点1 → 経由地i
* 経由地i → 終点1
同じ様にしてi=1として求めるとコスト0になってしまい、これは往復ではない。
こういう場合にはスタート地点をキューに入れるのではなく、スタート地点の次に移動可能なノードをキューに積みダイクストラする。

```python
import heapq
INF = 10 ** 9

def main():
    N, M = map(int, input().split())
    edge = [[] for _ in range(N)]
    
    for _ in range(M):
        a, b, c = map(int, input().split())
        edge[a - 1].append((c, b - 1))
    for s in range(N):
        h = []
        costs = [INF] * N
        for c, v in edge[s]:
            h.append((c, v))
            costs[v] = min(c, costs[v])
        heapq.heapify(h)
        while len(h) > 0:
            cost, now = heapq.heappop(h)
            if cost > costs[now]:
                continue
            for c, next in edge[now]:
                if costs[next] > costs[now] + c:
                    costs[next] = costs[now] + c
                    heapq.heappush(h, (costs[next], next))
        print(-1 if costs[s] == INF else costs[s])
    return
if __name__ == '__main__':
    main()
```

# ベルマン・フォード法

理論/理解
https://yttm-work.jp/algorithm/algorithm_0012.html

ダイクストラは負の重みがある辺が存在する場合には利用できない。
ベルマンフォード法では、その時点で確定しているノードのコストを正としてそれぞれのノードから移動可能なノードのコストを決めていく。
当然、既に評価したノードのコストを更新したことでそのノードを正として算出したノードのコストを再計算しないといけないケースが出てくる。
そのため、ベルマンフォード法では全頂点からスタートを除いた(V-1)回まで、更新がある限りこの一連の処理を繰り返す。
ただし、負閉路を含む場合、この更新は無限に終わらない。そのため、(V-1)回の更新に到達しても更新が終わらない場合は負閉路が含まれると判断できる。

問題
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B&lang=ja

```python:これまでのグラフの表現
INF = 10 ** 9

def main():    
    V, E, r = map(int, input().split())
    edge = [[] for _ in range(V)]
    costs = []
    for _ in range(E):
        s, t, d = map(int, input().split())
        edge[s].append((d, t))

    costs = [INF for _ in range(V)]
    costs[r] = 0
    loopCount = 0
    while True:
        loopCount += 1
        isUpdated = False
        for now in range(V):
            for cost, next in edge[now]:
                if costs[now] != INF and costs[next] > costs[now] + cost:
                    costs[next] = costs[now] + cost
                    isUpdated = True
        if not isUpdated:
            break
        elif loopCount == V - 1:
            print("NEGATIVE CYCLE")
            return
    
    for c in costs:
        print("INF" if c == INF else c)

if __name__ == '__main__':
    main()
```

ベルマンフォード法では全ての辺について見れればいいのでリストに辺の情報を並べるだけでも十分。

```python:edgeをリストにするのみ
INF = 10 ** 9

def main():    
    V, E, r = map(int, input().split())
    edges = []
    costs = []
    for _ in range(E):
        s, t, d = map(int, input().split())
        edges.append((s, t, d))

    costs = [INF for _ in range(V)]
    costs[r] = 0
    loopCount = 0
    while True:
        loopCount += 1
        isUpdated = False
        for s, t, d in edges:
            if costs[s] != INF and costs[t] > costs[s] + d:
                costs[t] = costs[s] + d
                isUpdated = True
        if not isUpdated:
            break
        elif loopCount == V - 1:
            print("NEGATIVE CYCLE")
            return
    
    for c in costs:
        print("INF" if c == INF else c)

if __name__ == '__main__':
    main()
```

```python
INF = 10 ** 9

def main():    
    V, E, r = map(int, input().split())
    edges = []
    costs = []
    for _ in range(E):
        s, t, d = map(int, input().split())
        edges.append((s, t, d))

    costs = [INF] * V
    costs[r] = 0
    for i in range(V):
        for s, t, d in edges:
            if costs[s] != INF and costs[t] > costs[s] + d:
                costs[t] = costs[s] + d
                if i == V - 1:
                    print("NEGATIVE CYCLE")
                    return
    
    for c in costs:
        print("INF" if c == INF else c)

if __name__ == '__main__':
    main()
```

## テンプレート

キューやスタックといったデータ構造は出てこない。実装は楽。

```
# 作成と初期化
## リスト(1)作成   -> フィールドを表す2次元リストを生成 (入力から受け取る)
## リスト(2)作成   -> [コスト]用 初期値はスタート地点のみ0、それ以外はINF

# 探索 (以下を更新がなくなるまで繰り返す)
## 全ての辺について以下の場合は更新する。
###   * 移動元となるノードが初期値INFでないこと。
###   * そこにいくことで最小コストを更新できること。(リスト2)
## 上記の更新をV-1回繰り返してなお更新がある場合 = 負閉路あり
```

問題
https://atcoder.jp/contests/abc061/tasks/abc061_d

```python
INF = 10 ** 16

def main():
    N, M = map(int, input().split())
    edges = []
    costs = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((a - 1, b - 1, -c))

    costs = [INF] * N
    costs[0] = 0
    for loopCount in range(N):
        for a, b, c in edges:
            if costs[a] != INF and costs[b] > costs[a] + c:
                costs[b] = costs[a] + c
                if loopCount == N - 1 and b == N - 1:
                    print("inf")
                    return

    print(-costs[N - 1])


if __name__ == '__main__':
    main()
```