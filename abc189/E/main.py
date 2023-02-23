#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().rstrip()

# COPIED FROM https://atcoder.jp/contests/abc189/submissions/38873526
from math import sin, cos, radians
class AffineMap():
    NEW = [
        [1, 0, 0], 
        [0, 1, 0], 
        [0, 0, 1]
    ]
    @staticmethod
    def new():
        return AffineMap.NEW[:]

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
    def rotate(a: "list[int]", digree: int = 0):
        """
        回転
        degree度(度数法)回転する。
        """
        if digree == 90:
            b = [
                [0, -1, 0], 
                [1, 0, 0], 
                [0, 0, 1]
            ]
        elif digree == -90:
            b = [
                [0, 1, 0], 
                [-1, 0, 0], 
                [0, 0, 1]
            ]
        else:
            digree = radians(digree)
            b = [[cos(digree), -sin(digree), 0], [sin(digree), cos(digree), 0], [0, 0, 1]]
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

N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
matrix = AffineMap.new()
memo = [matrix]
for _ in range(M):
    op = list(map(int, input().split()))
    t = op[0]
    if t == 1:
        matrix = AffineMap.rotate(matrix, -90)
    elif t == 2:
        matrix = AffineMap.rotate(matrix, 90)
    elif t == 3:
        matrix = AffineMap.x_symmetrical_move(matrix, op[1])
    else:
        matrix = AffineMap.y_symmetrical_move(matrix, op[1])
    memo.append(matrix)

Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    print(*AffineMap.get(memo[A], *XY[B - 1]))
