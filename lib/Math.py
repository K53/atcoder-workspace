# ------------------------------------------------------------------------------
#     Mathリスト
# ------------------------------------------------------------------------------
# - 直交座標の回転
# - 二次元配列の回転と反転
# - N進数変換
# - 外積 (2つのベクトルABとCDが交差するかの判定)
# - 数列の和の公式
# - 順列

# ------------------------------------------------------------------------------
#     直交座標の回転
# ------------------------------------------------------------------------------
# - 一般式
#   - 点(cur_X, cur_Y)を点(x0, y0)を中心にθ度回転した後の点(new_X, new_Y)
#   　new_X - x0 = (cur_X - x0) * cosθ - (cur_Y - y0) * sinθ
#   　new_Y - y0 = (cur_X - x0) * sinθ + (cur_Y - y0) * cosθ
#
# - point
#   - 90度回転などの場合、誤差が出るのでsinやcosではなく最初から整数値で計算するべき。
# 
# - 参考
#   - https://mathwords.net/heimenkaiten
# 
# - verify
#   - https://atcoder.jp/contests/abc275/tasks/abc275_c
# ------------------------------------------------------------------------------

#           ↑y
#           |   ■ Current
#   □(1)    |
#           |
#           |
# ----------+----------->x
#           |
#           |
#           |      □(2)
#
# (1) 正の方向(反時計回り90度回転)
x0, y0 = 0, 0
cur_X, cur_Y = 3, 4
new_X = (cur_X - x0) * 0 + (cur_Y - y0) * -1 + x0
new_Y = (cur_X - x0) * 1 + (cur_Y - y0) * 0 + y0
print(new_X, new_Y) # -4, 3

# (2) 正の方向(反時計回り90度回転)
x0, y0 = 0, 0
cur_X, cur_Y = 3, 4
new_X = (cur_X - x0) * 0 + (cur_Y - y0) * 1 + x0
new_Y = (cur_X - x0) * -1 + (cur_Y - y0) * 0 + y0
print(new_X, new_Y) # 4, -3


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

# 転置
# 縦方向の並びを横方向に並べ直したもの。
transposed = list(zip(*original))
print(transposed)
"""
[
    ('1', '8', '7'), 
    ('2', '9', '6'), 
    ('3', '4', '5')
]
"""


# ------------------------------------------------------------------------------
#     N進数変換 (K進数 -> 10 進数) (2 <= K <= 10)
# ------------------------------------------------------------------------------
def baseKto10int(baseKvalue: int, fromBase: int):
    """
    - fromBase : N進数
    - baseKvalue : N進数表記された数値
    ${fromBase}進数の数である${baseKvalue}を10進数で表した数値を得る。
    """
    ans = 0
    exp = 0
    baseKvalue = list(str(baseKvalue)) 
    for i in baseKvalue[::-1]:
        ans += int(i) * fromBase ** exp
        exp += 1
    return ans

val = 12
K = 7
print(baseKto10int(baseKvalue=val, fromBase=K)) # -> 9

# 2/8/16進数 -> 10進数は組み込み関数あり。
base2value: str = str(10)
K = 2
print(int(base2value ,K)) # 2,8,16のみ
"""-> 2 """

# ------------------------------------------------------------------------------
#     N進数変換 (10進数 -> K 進数) (2 <= K <= 10)
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
print(base10toKint(base10value=val, toBase=K)) # -> 15


# ------------------------------------------------------------------------------
#     外積
# ------------------------------------------------------------------------------
# 2つのベクトルABとCDが交差するかの判定
#
# 解説 -> https://qiita.com/zu_rin/items/e04fdec4e3dec6072104
# ------------------------------------------------------------------------------

def outerProduct(A_x: int, A_y: int, B_x: int, B_y: int, C_x: int, C_y: int, D_x: int, D_y: int):
    s = (B_x-A_x) * (C_y-A_y) - (C_x-A_x) * (B_y-A_y)
    t = (B_x-A_x) * (D_y-A_y) - (D_x-A_x) * (B_y-A_y) 
    return s * t # < 0 であれば2つのベクトルABとCDは交差する。


# ------------------------------------------------------------------------------
#     数列の和
# ------------------------------------------------------------------------------
#
#
# - ref
#   https://rikeilabo.com/formula-list-of-arithmetic-progression
#   https://rikeilabo.com/formula-list-of-geometric-progression
# ------------------------------------------------------------------------------

# 等差数列(初項a0, 末項l, 項数n)
def getArithmeticSequenceSum(a0: int, l: int, n: int):
    return (a0 + l) * n // 2

# 等差数列(初項a0, 公差d, 項数n)
def getArithmeticSequenceSum(a0: int, d: int, n: int):
    return (2 * a0 + (n - 1) * d) * n // 2

# 等比数列(初項a0, 公比r, 項数n)
def getGeometricSequenceSum(a0: int, r: int, n: int):
    if r == 1:
        return a0 * n
    return a0 * (1 - pow(r, n)) // (1 - r)


# ------------------------------------------------------------------------------
#     面積
# ------------------------------------------------------------------------------
# - https://mathwords.net/x1y2hikux2y1
#
# ------------------------------------------------------------------------------

def getAria(
    x_1: int, y_1: int,
    x_2: int, y_2: int,
    x_O: int = 0, y_O: int = 0,
    ) -> int:
    return abs((x_1 - x_O) * (y_2 - y_O) - (x_2 - x_O) * (y_1 - y_O)) / 2

# ------------------------------------------------------------------------------
#     任意の順列 ⇆ 全順列の昇順K番目 変換
# ------------------------------------------------------------------------------
# - 参考
#   https://atcoder.jp/contests/abc276/editorial/5189
# ------------------------------------------------------------------------------

class PermutationFactory():
    def __init__(self, N: int) -> None:
        """
        階乗算出
        O(N)
        """
        self.N = N
        self.fac = [1, 1] # 階乗リスト
        for i in range(2, N + 1):
            self.fac.append(self.fac[i - 1] * i)
        return
    
    def kth_permutation(self, k: int) -> list:
        """
        k番目の順列を返す。O(N)
        先頭要素から固定していく。その要素を固定したときの順列の場合の和をkから引いていく。
        args:
            k: 0〜(N-1)の順列の昇順k番目 (0-index)
        return:
            res: k番目のリスト
        """
        candidates = list(range(self.N)) # 任意の配列でもいいが重複がないこと
        res = []
        for i in reversed(range(self.N)):
            a = self.fac[i]
            # print(a)
            j, k = divmod(k, a)
            res.append(candidates[j])
            del candidates[j]
        return res

    def get_kth_of_permutation(self, L: list) -> int:
        """
        args:
            L: 0〜(N-1)までの順列で昇順何番目かを求めたい順列
        return:
            k: 昇順何番目か (0-index)
        """
        k = 0
        while len(L) > 1:
            a = len([ll for ll in L if ll < L[0]])
            k += a * self.fac[len(L) - 1]
            L = L[1:]
        return k

# usage
P = [0, 1, 3, 2]
pf = PermutationFactory(len(P))
print(pf.get_kth_of_permutation(P)) # 1
print(pf.kth_permutation(0)) # [0, 1, 2, 3]
print(pf.kth_permutation(1)) # [0, 1, 3, 2]
print(pf.kth_permutation(2)) # [0, 2, 1, 3]
