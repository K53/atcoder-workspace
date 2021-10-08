# ------------------------------------------------------------------------------
#     座標圧縮
# ------------------------------------------------------------------------------
# 解説
# 1. 重複を排除後にソート。
# 2. 小さい要素valから順にナンバリング(listのindexを適用)。→ 0-index
# 3. 元の要素がどの圧縮後のindexに対応するかの辞書に変更 → なお、ここで1を加算したら1-index。
#
# - 出現しうる要素の範囲が大きく単純にバケット法が利用できないが、1テストケースあたりの要素数の最大数は少ない場合に利用可能。
# 
# Order
#   O(len(L))
#
# verify
# - https://atcoder.jp/contests/abc213/tasks/abc213_c (一方向)
# - https://atcoder.jp/contests/abc036/tasks/abc036_c (一方向)
# - https://atcoder.jp/contests/abc221/tasks/abc221_d (双方向)
# ------------------------------------------------------------------------------

# 一方向 (復元できない)
L = [9, 5, 2, 6]
compressed = {val : index for index, val in enumerate(sorted(list(set(L))))}
print(compressed)
"-> {2: 0, 5: 1, 6: 2, 9: 3}"
print(len(list(compressed))) # 要素の長さ
"-> 4"

# 双方向 (復元用リストも作成する)
compressed = {}
compressed_to_row = []
for index, val in enumerate(sorted(list(set(L)))):
    compressed[val] = index
    compressed_to_row.append(val)
print(compressed)
"-> {2: 0, 5: 1, 6: 2, 9: 3}"
print(compressed_to_row)
"-> [2, 5, 6, 9]"
print(len(compressed_to_row)) # 要素の長さ
"-> 4"