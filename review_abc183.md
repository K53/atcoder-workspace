# C

## 順列列挙

`itertools.permutations`を用いることで順列を列挙できる。
https://note.nkmk.me/python-math-factorial-permutations-combinations/

```
import itertools

l = [0, 1, 2]
for v in itertools.permutations(l):
    print(v)
# 個々はタプルで返却される。
# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)

# 第二引数を指定すると選択する個数を指定できる。
for v in itertools.permutations(l, 2):
    print(v)
# (0, 1)
# (0, 2)
# (1, 0)
# (1, 2)
# (2, 0)
# (2, 1)

# なお重複順列は非対応 (indexで区別しているため同じ値かどうかは見ていない。)
h = [1, 1]
for v in itertools.permutations(l, 2):
    print(v)
# (1, 1)
# (1, 1)
```

# D

考え方:

同時に評価する <- (変換することで高速になるかを考える) ->  時系列順に評価する

1分あたりに消費するお湯の量を求める = 同時に評価する
-> N人目のt分目の消費量を求めるにはO(Nt)



絶対量か相対変化量か?