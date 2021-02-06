# B

`-x < y < x`のような条件を愚直に実装すると、xが負かどうかを判別して左右を入れ替える処理を挟む必要が出てくる。
これを`abs(y) < abs(x)`のようにすることでその手間を省ける。

# C

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