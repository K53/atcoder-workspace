# ------------------------------------------------------------------------------
#     2次元配列回転
# ------------------------------------------------------------------------------
# - verify
#   - https://atcoder.jp/contests/abc107/tasks/abc107_b (時計・反時計)
# ------------------------------------------------------------------------------


original = [
    ('1', '2', '3'), 
    ('8', '9', '4'), 
    ('7', '6', '5')
]

# 90度時計回り回転 (+90)
clockwiseRotated = list(zip(*original[::-1]))
print(clockwiseRotated)
"""
[
    ('7', '8', '1'), 
    ('6', '9', '2'), 
    ('5', '4', '3')
]
"""

# 90度反時計回り回転 (+270)
counterClocwiseRotate = list(zip(*[o[::-1] for o in original]))
"""
[
    ('3', '4', '5'), 
    ('2', '9', '6'), 
    ('1', '8', '7')
]
"""
print(counterClocwiseRotate)

# 180度回転
rotated180 = [o[::-1] for o in original][::-1]
print(rotated180)
"""
[
    ('5', '6', '7'), 
    ('4', '9', '8'), 
    ('3', '2', '1')
]
"""

# 左右反転
flipHorizontal = [o[::-1] for o in original]
print(flipHorizontal)
"""
[
    ('3', '2', '1'), 
    ('4', '9', '8'), 
    ('5', '6', '7')
]
"""

# 上下反転
flipVertical = [o for o in original][::-1]
"""
[
    ('7', '6', '5'), 
    ('8', '9', '4'), 
    ('1', '2', '3')
]
"""
print(flipVertical)

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