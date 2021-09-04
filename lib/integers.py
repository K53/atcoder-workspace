# ------------------------------------------------------------------------------
#     約数列挙
# ------------------------------------------------------------------------------
# 解説
# - √Nまで貪欲に確認。 
# 
# 注意 !Attention! 
# - N要素全てに対して約数列挙する場合はエラトステネスの篩を利用した高速約数列挙を利用せよ。
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
    while i * i <= n: # sqrt(N)まで試し割りする。
        if n % i == 0:
            lowerDivisors.append(i)
            if i != n // i:
                upperDivisors.append(n//i)
        i += 1
    return lowerDivisors + upperDivisors[::-1]

# usage
print(getDivisors(120))
"-> [1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120]"


# ------------------------------------------------------------------------------
#     素因数分解
# ------------------------------------------------------------------------------
# 解説
# - √Nまで貪欲に確認。
# 
# 注意 !Attention! 
# - N要素全てに対して約数列挙する場合はエラトステネスの篩を利用した高速素因数分解を利用せよ。
# 
# リンク
# - 
# 
# 計算量
# - O(√N)
# 
# Modify
# - 
# ------------------------------------------------------------------------------
def primeFactorise(n: int) -> list:
    primeFactors = []
    i = 2
    while i * i <= n: # sqrt(N)まで試し割りする。
        exp = 0
        while n % i == 0:
            exp += 1
            n //= i
        if exp != 0:
            primeFactors.append((i, exp))
        i += 1
    if n != 1:
        primeFactors.append((n, 1))
    return primeFactors

# Usage
l = primeFactorise(90)
print(l)
"-> [(2, 1), (3, 2), (5, 1)]"
# convert to dict
print(dict(l))
"-> {2: 1, 3: 2, 5: 1}"