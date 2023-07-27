# ------------------------------------------------------------------------------
#     Affine Transformation (アフィン変換)
# ------------------------------------------------------------------------------
# 解説
# 座標平面に対し回転や平行移動の操作を行うクエリと、任意の座標の移動後の位置を求めるクエリが繰り返される場合。
# 各座標に対して操作を行うのは重いので、原点(0,0)と任意の2点(1,0)/(0,1)の3点の移動だけを追跡しておき、
# 任意の座標の移動後の座標を即座に計算できるようにする。
# 
# verify
#  
# ------------------------------------------------------------------------------

# COPIED FROM https://atcoder.jp/contests/abc189/submissions/38873526
from math import sin, cos, radians
class AffineMap():
    origin = [
        [1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 1]
    ]
    @staticmethod
    def generateOrigin():
        """
        原点座標を取得する。
        """
        return AffineMap.origin[:]

    @staticmethod
    def _matmul3(a: "list[list[int]]", b: "list[list[int]]"):
        res = [
            [0, 0, 0], 
            [0, 0, 0], 
            [0, 0, 0]
        ]
        for i in range(3):
            for k in range(3):
                aik = a[i][k]
                for j in range(3):
                    res[i][j] += b[k][j] * aik
        return res

    @staticmethod
    def shift(a: "list[int]", shift_x: int = 0, shift_y: int = 0):
        b = [
            [1, 0, shift_x], 
            [0, 1, shift_y], 
            [0, 0, 1]
        ]
        return AffineMap._matmul3(b, a)

    @staticmethod
    def expand(a: "list[int]", ratio_x: int = 1, ratio_y: int = 1):
        b = [
            [ratio_x, 0, 0], 
            [0, ratio_y, 0], 
            [0, 0, 1]
        ]
        return AffineMap._matmul3(b, a)

    @staticmethod
    def rotate(a: "list[int]", center_x: int = 0, center_y: int = 0, digree: int = 0):
        """
        回転
        degree度(度数法)回転する。
        """
        if digree == 90:
            b = [
                [0, -1, center_x + center_y], 
                [1, 0, center_y - center_x], 
                [0, 0, 1]
            ]
        elif digree == -90:
            b = [
                [0, 1, center_x - center_y], 
                [-1, 0, center_y + center_x], 
                [0, 0, 1]
            ]
        else:
            digree = radians(digree)
            b = [
                [cos(digree), -sin(digree), center_x - center_x * cos(digree) + center_y * sin(digree)], 
                [sin(digree), cos(digree), center_y - center_x * sin(digree) - center_y * cos(digree)], 
                [0, 0, 1]
            ]
        return AffineMap._matmul3(b, a)
    
    @staticmethod
    def x_symmetrical_move(a: "list[int]", p: int):
        """
        対称移動
        直線 x = p で対称移動する。
        """
        b = [
            [-1, 0, 2 * p], 
            [0, 1, 0], 
            [0, 0, 1]
        ]
        return AffineMap._matmul3(b, a)

    @staticmethod
    def y_symmetrical_move(a: "list[int]", p: int):
        """
        対称移動
        直線 y = p で対称移動する。
        """
        b = [
            [1, 0, 0], 
            [0, -1, 2 * p], 
            [0, 0, 1]
        ]
        return AffineMap._matmul3(b, a)

    @staticmethod
    def get(a: "list[list[int]]", x, y):
        """
        点(x, y)を変換行列aを用いて変換後の頂点の座標を返す。
        """
        a0, a1, a2 = a
        x, y = a0[0] * x + a0[1] * y + a0[2], a1[0] * x + a1[1] * y + a1[2]
        return x, y

# Usage
matrix = AffineMap.generateOrigin() # (0, 0), (1, 0), (0, 1)の3点の変化を記録する行列

print(AffineMap.get(matrix, x=1, y=10)) # 何もしていない状態では (x, y) = (1, 10)

# 初期値は以下
# [
#     [1, 0, 0], 
#     [0, 1, 0], 
#     [0, 0, 1]
# ]

# 反時計回りに90度回転
matrix = AffineMap.rotate(matrix, digree=-90)

print(AffineMap.get(matrix, x=1, y=10))  # 90度回転後は (x, y) = (10, -1)

# 直線 x = 3 で対称移動
#   |   |
#   |   |
#   | * |→  * (対称移動)
#   |   |
#   |   |
#  -+---+---------------
#   |0  |3
#
matrix = AffineMap.x_symmetrical_move(matrix, 3)

print(AffineMap.get(matrix, x=1, y=10)) # 90度回転後は (x, y) = (-4, -1)

#--------
print("-------------------------------------")
print("任意の1点(2, 3)の変換をするだけでいい場合。")

matrix = AffineMap.generateOrigin() # (0, 0), (1, 0), (0, 1)の3点の変化を記録する行列
print(AffineMap.get(matrix, x=10, y=10)) # S(10, 10)
matrix = AffineMap.rotate(matrix, center_x=15, center_y=15, digree=90)
print(matrix)
print(AffineMap.get(matrix, x=10, y=10)) # G(20, 10)

#               y
#               ↑
#               |
#               |        ・ (15, 15)
#               |     
#               |   *S    →     *G
#               |   (10, 10)    (20, 10)
# --------------+------------------> x
#               |
#               |
#               |
#               |
#               |