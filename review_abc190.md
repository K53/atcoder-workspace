# C

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

# D

等差部分数列の和S

n = (項数)
d = (公差)
a = (初項)
l = (末項) = a + (n - 1) * d

S = (a + l) * n * 1/2
  = (2a + (n - 1)d) * n / 2

今回のD問題ではd = 1、S = Nのため以下の様になる。

N = (2a + n - 1) * n / 2

x = 2a + n - 1
y = n

とすると N = x * y / 2 である。

ここで、Nは整数であることからxまたはyは偶数である必要がある。

すなわち、
y = n = 偶数であるとき、x = 奇数
y = n = 奇数であるとき、x = 偶数
となる。

この分け方に従い、Nを因数分解し偶奇を振り分ける。

素因数分解
https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8

```python
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
```

素因数2に関してはいくつあっても関係なく、xに全振りするかyに全振りするかの2通り。
その他の素因数はそれぞれx:yにいくつずつ割り振るかなので、それぞれ[個数]+1通り。
