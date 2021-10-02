# ------------------------------------------------------------------------------
#     組み合わせ(Compination, nCr)
# ------------------------------------------------------------------------------
# 解説
# - 組み合わせの総数を出力。
# 
# リンク
# - 
# 
# 計算量
# - O(log(r))以下程度(概算)
# - https://qiita.com/ageprocpp/items/f6661deaa09dda124132
# 
# verify
# - https://atcoder.jp/contests/abc185/tasks/abc185_c
# - https://atcoder.jp/contests/abc034/tasks/abc034_c
# ------------------------------------------------------------------------------
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
            for k in range(p - 1, r, p):            # p番目を約分できるということはp番目からpの倍数番目も約分可能なので実施する。
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
 
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result


# Udage
print(cmb(10, 2)) # = 10C2 = 10 * 9 // 2 * 1
"-> 45"