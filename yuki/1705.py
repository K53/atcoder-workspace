#!/usr/bin/env python3
import sys

MOD = 998244353

class SegTree:
    def __init__(self, monoid, bottomList, func):
        self.monoid = monoid
        self.func = func
        self.bottomLen = len(bottomList)
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen
        self.build(bottomList)

    """
    初期化
    O(self.segLen)
    """
    def build(self, seq):
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])

    """
    一点更新
    O(log(self.bottomLen))
    """
    def pointUpdate(self, i: int, val: int):
        i += self.offset
        self.tree[i] = val
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

    """ 区間取得
    O(log(self.bottomLen))
    """
    def getRange(self, l: int, r: int): # r含まない
        l += self.offset
        r += self.offset
        vL = (self.monoid, 0)
        vR = (self.monoid, 0)
        while l < r:
            if l & 1:
                vL = self.func(vL, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                vR = self.func(self.tree[r], vR)
            l >>= 1
            r >>= 1
        return self.func(vL, vR)

    """ 一点取得
    O(log(self.bottomLen))
    """
    def getPoint(self, i: int):
        i += self.offset
        return self.tree[i]

def f(x: tuple, y: tuple):
    if x[0] > y[0]:
        return x
    elif x[0] == y[0]:
        if x[1] > y[1]:
            return x
        else:
            return y
    else:
        return y

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    Q = int(input())
    seg = SegTree(0, [(aa, i) for i, aa in enumerate(A)], f)
    for _ in range(Q):
        t, x, y = list(map(int, input().split()))
        if t == 1:
            num, _ = seg.getPoint(x - 1)
            seg.pointUpdate(x - 1, (num + y, x - 1))
        elif t == 2:
            num, _ = seg.getPoint(x - 1)
            seg.pointUpdate(x - 1, (num - y, x - 1))
        else:
            print((seg.getRange(0, M))[1] + 1)
    return

if __name__ == '__main__':
    main()
