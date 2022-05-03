#!/usr/bin/env python3
import sys

MOD = 998244353

class SegTree:
    def __init__(self, monoid, N, func):
        self.monoid = monoid
        self.func = func
        self.bottomLen = N
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen

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
    一点加算 他演算
    O(log(self.bottomLen))
    """
    def pointAdd(self, i: int, val: int):
        i += self.offset
        self.tree[i] += val
        # self.tree[i] = self.func(self.tree[i], val) <- こっちの方が都度の修正は発生しない。再帰が遅くないか次第。
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

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
    
    """
    区間更新
    O(log(self.bottomLen))
    """
    def rangeAdd(self, l: int, r: int, val: int):
        l += self.offset
        r += self.offset
        while l < r:
            if l & 1:
                self.tree[l] = self.func(self.tree[l], val) 
                l += 1
            if r & 1:
                r -= 1
                self.tree[r] = self.func(self.tree[r], val) 
            l >>= 1
            r >>= 1
        return

    """ 区間取得
    O(log(self.bottomLen))
    """
    def getRange(self, l: int, r: int):
        l += self.offset
        r += self.offset
        vL = self.monoid
        vR = self.monoid
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


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    monoid = (10 ** 6, 0)
    def func(x: tuple, y: tuple):
        return x if x[0] < y[0] else y
    seg = SegTree(monoid, N, func)
    seg.build([(aa, i) for i, aa in enumerate(A)])
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            l, r = query[1] - 1, query[2] - 1
            ll, _ = seg.getPoint(l)
            rr, _ = seg.getPoint(r)
            seg.pointUpdate(r, (ll, r))
            seg.pointUpdate(l, (rr, l))
        else:
            l, r = query[1] - 1, query[2] - 1
            _, ans = seg.getRange(l, r + 1)
            print(ans + 1)
    return

if __name__ == '__main__':
    main()
