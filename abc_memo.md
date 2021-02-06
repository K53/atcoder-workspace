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