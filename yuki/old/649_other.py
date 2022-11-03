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

    """
    二分探索
    O(log(self.bottomLen))
    ※ セグ木上の二分探索を使う場合は2べきにすること。
    """
    def queryKthItem(self, K: int):
        # print("セグ木上の二分探索を使う場合は2べきにすること。")
        index = 1
        restK = K
        while index < self.offset:
            if restK <= self.tree[index << 1]:
                index <<= 1
            else:
                restK -= self.tree[index << 1] # 左に進む場合は右側の分を差し引く。
                index <<= 1
                index += 1
        return index - self.offset

def main():
    Q, K = map(int, input().split())
    queries = []
    c = set()
    for _ in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)
        if query[0] == 1:
            c.add(query[1])
    compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(sorted(list(c))):
        compressed[val] = index
        compressed_to_raw.append(val)
            
    def add(x: int, y: int):
        return x + y
    def getSegLenOfThePowerOf2(ln: int):
        if ln <= 0:
            return 1
        else:    
            import math
            decimalPart, integerPart = math.modf(math.log2(ln))
            return 2 ** (int(integerPart) + 1)


    seglen = getSegLenOfThePowerOf2(len(compressed.keys()))
    seg = SegTree(0, [0] * seglen, add)
    segsum = 0

    for query in queries:
        if query[0] == 1:
            seg.pointAdd(compressed[query[1]], 1)
            segsum += 1
        else:
            # print(seg.tree)
            if segsum < K:
                print(-1)
                continue
            num = seg.queryKthItem(K)
            seg.pointUpdate(num, seg.getPoint(num) - 1)
            segsum -= 1
            print(compressed_to_raw[num])
    return

if __name__ == '__main__':
    main()
