# ------------------------------------------------------------------------------
#     約数列挙
# ------------------------------------------------------------------------------
# 解説
# - √Nまで貪欲に確認。
# 
# リンク
# - ノーマルなダブリング→ https://qiita.com/Kept1994/items/ea91c057b0e552323da3
# - 総和のダブリング→ https://qiita.com/Kept1994/items/fa3917f2812f1a3f5f96
# 
# 計算量
# - O(√N)
# 
# Modify
# - https://yukicoder.me/problems/no/1452
# ------------------------------------------------------------------------------
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

# usage
print(getDivisors(120))
"-> [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]"
