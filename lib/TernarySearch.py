# ------------------------------------------------------------------------------
#     三分探索 (Ternary Search)
# ------------------------------------------------------------------------------
# 解説
#  - 関数fの定義域が整数の場合、
#
# 参考
#  - https://qiita.com/DaikiSuyama/items/84df26daad11cf7da453
# verify
#  - https://atcoder.jp/contests/arc054/tasks/arc054_b
#  - https://atcoder.jp/contests/arc122/tasks/arc122_b
#  - https://atcoder.jp/contests/past202104-open/tasks/past202104_j
#  - https://atcoder.jp/contests/abc279/tasks/abc279_d (定義域が整数なので割り切って使う問題)
#  - https://atcoder.jp/contests/abc102/tasks/arc100_a (定義域が整数なので割り切って使う問題)
#  - https://atcoder.jp/contests/abc151/tasks/abc151_f (二重三分探索/二次元の座標空間で三分探索)
# ------------------------------------------------------------------------------
# 最小にしたい関数f (例: 10/√(k + 1) + k)
def f(k: float or int) -> float:
    return 10 / pow(k + 1, 1/2) + k
    
def ternarySearch(l: float, r: float, accept_range: int = 2) -> tuple:
    """
    - l : 定義域(l ≦ x ≦ r)の左端
    - r : 定義域(l ≦ x ≦ r)の右端
    - accept_range : 探索で絞った後の範囲
    三分探索を行い、最小値を取る値の範囲l ~ rを返却する。
    """
    # 範囲が accept_range 以下に絞られるまで回す。
    while r - l > accept_range:
        # オーバーフローしないための三等分点を置く
        mid1 = l + (r - l) / 3 # 探索する値の定義域が整数の場合は // として割り切る。
        mid2 = r - (r - l) / 3 # 探索する値の定義域が整数の場合は // として割り切る。
        if f(mid1) < f(mid2):
            r = mid2
        else:
            l = mid1
    return (l, r)

import math
l, r = ternarySearch(l=0, r=10 ** 18, accept_range=pow(10, -8)) # pow(10, -8)の誤差を許容。
print(f(l)) # -> 7.772053214638598 : 関数fの値が小数(誤差10^-8を許容)を含む場合の最小値。

l, r = ternarySearch(l=0, r=10 ** 18) # 関数fの値が整数のみの場合の最小値。周辺の整数を探索する。
ans = 10 ** 18
for i in range(math.floor(l), math.ceil(r)):
    ans = min(ans, f(i))
print(ans) # -> 7.773502691896258 : 関数fの値が整数のみの場合の最小値。