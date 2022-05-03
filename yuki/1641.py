#!/usr/bin/env python3
from collections import defaultdict
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
    
    # """ # 未検証 多分動かない -> LazySegmentTreeへ
    # 区間更新
    # O(log(self.bottomLen))
    # """
    # def rangeUpdate(self, l: int, r: int, val: int):
    #     l += self.offset
    #     r += self.offset
    #     while l < r:
    #         if l & 1:
    #             self.tree[l] = self.func(self.tree[l], val) 
    #             l += 1
    #         if r & 1:
    #             r -= 1
    #             self.tree[r] = self.func(self.tree[r], val) 
    #         l >>= 1
    #         r >>= 1
    #     return

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
    区間取得
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

    """
    一点取得
    O(log(self.bottomLen))
    """
    def getPoint(self, i: int):
        i += self.offset
        return self.tree[i]

def main():
    N, Q = map(int, input().split())
    C = list(map(int, input().split()))
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    
    eularTourNodes = []
    sys.setrecursionlimit(10 ** 9)
    def getEularTourNodes(now: int, pre: int = -1):
        eularTourNodes.append(now) # ノードから葉の方へ出る時に記録
        for next in G[now]:
            if next == pre:
                continue
            getEularTourNodes(next, now) 
        eularTourNodes.append(now) # ノードから根に戻る時に記録 (Path.B)
        return
    getEularTourNodes(0)
    d = defaultdict(list)
    for i, num in enumerate(eularTourNodes):
        d[num].append(i)
    # print(d)
        



    # print("-----")
    # print("eularTourNodes", eularTourNodes)
    # print("-----")

    def add(x, y):
        return x + y
    
    seg = [SegTree(0, [0] * (N * 2), add) for _ in range(10)]
    for i, cc in enumerate(C):
        for bit in range(10):
            for idx in d[i]:
                seg[bit].pointUpdate(idx, (cc >> bit) & 1)
    # for i in range(10):
    #     print(seg[i].tree)
    # print("---")

    for _ in range(Q):
        t, x, y = list(map(int, input().split()))
        x -= 1
        if t == 1:
            for bit in range(10):
                for idx in d[x]:
                    num = seg[bit].getPoint(idx)
                    seg[bit].pointUpdate(idx, num ^ ((y >> bit) & 1))
            # for i in range(10):
            #     print(seg[i].tree)
            # print("---")
        else:
            l, r = d[x]
            ans = 0
            for bit in range(10):
                ans += ((seg[bit].getRange(l, r + 1) // 2) % 2) * (2 ** bit)
            print(ans)
    return

if __name__ == '__main__':
    main()