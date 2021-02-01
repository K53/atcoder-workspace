# C

コンビネーション(nCr)の算出。

```python
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r + 1):                    # p番目について、
        pivot = denominator[p - 1]              # pivot(その時の分母)で約分を試みる。
        if pivot > 1:                           # ただし、pivotが1、すなわち既に割り尽くされているならp番目は飛ばす。
            offset = (n - r) % p                # pの倍数の先頭からの位置調整
            for k in range(p-1,r,p):            # p番目を約分できるということはp番目からpの倍数番目も約分かのうなので実施する。
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
```

```python:確認用
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
        pivot = denominator[p - 1]              # pivot(その時の分母)で約分を試みる。
        # print("--- p  : " + str(p))
        # print("--- piv: " + str(pivot))
        if pivot > 1:                           # ただし、pivotが1、すなわち既に割り尽くされているならp番目は飛ばす。
            offset = (n - r) % p                # pの倍数の先頭からの位置調整
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
```

# D

標準のsort()はO(nlogn)であるため今回2*10^5の要素も回すことが可能。
https://qiita.com/drken/items/18b3b3db5735241465ef
