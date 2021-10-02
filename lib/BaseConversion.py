# ------------------------------------------------------------------------------
#     N進数変換 (K進数 -> 10 進数) (2 <= K <= 10)
# ------------------------------------------------------------------------------
# 解説
# - 
# 
# リンク
# - 
# 
# 計算量
# 
# verify
# - 
# ------------------------------------------------------------------------------
def baseKto10int(baseKvalue: int, fromBase: int):
    ans = 0
    exp = 0
    baseKvalue = list(str(baseKvalue)) 
    for i in baseKvalue[::-1]:
        ans += int(i) * fromBase ** exp
        exp += 1
    return ans

val = 12
K = 7
num = baseKto10int(baseKvalue=val, fromBase=K)
print(num)
"""-> 9"""

# 2/8/16進数 -> 10進数は組み込み関数あり。
base2value: str = str(10)
K = 2
print(int(base2value ,K)) # 2,8,16のみ
"""-> 2 """

# ------------------------------------------------------------------------------
#     N進数変換 (10進数 -> K 進数) (2 <= K <= 10)
# ------------------------------------------------------------------------------
# 解説
# - 
# 
# リンク
# - 
# 
# 計算量
# 
# verify
# - 
# ------------------------------------------------------------------------------
def base10toKint(base10value, toBase):
    ans = []
    p = base10value
    while p >= toBase:
        p, q = divmod(p, toBase)
        ans.append(str(q))
    ans.append(str(p))
    return "".join(ans[::-1])

val = 12
K = 7
num = base10toKint(base10value=val, toBase=K)
print(num)
"""-> 15"""