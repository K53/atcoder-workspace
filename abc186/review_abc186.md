# C

```python:n進数に変換する標準関数
bin() # 2進数表記の文字列に変換
oct() # 8進数表記の文字列に変換
hex() # 16進数表記の文字列に変換

# 逆に文字列表記のn進数を10進数の数字に戻す時はintの第二引数に基数を指定する。

int("10", 8) # 8進数表記の"10"を10進数の数字に変換。

```

# D

→ 単位を揃えることで計算量を減らせる問題。
`(要素A - 要素C) = (A ー B) + (B - C)`と分解でき、最小単位である総和を求めるには各差分が何個存在するかを見ればいい。

