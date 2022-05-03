#!/usr/bin/env python3
import sys

MOD = 998244353

class SegTree:
    def __init__(self, monoid, bottomList, func, convertLengthToThePowerOf2: bool):
        self.monoid = monoid
        self.func = func
        if convertLengthToThePowerOf2:
            self.actualLen = len(bottomList)
            self.bottomLen = self.getSegLenOfThePowerOf2(len(bottomList))
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [monoid] * self.segLen
        else:
            self.actualLen = len(bottomList)
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
    直近の2べきの長さを算出
    """
    def getSegLenOfThePowerOf2(self, ln: int):
        if ln <= 0:
            return 1
        else:    
            import math
            decimalPart, integerPart = math.modf(math.log2(ln))
            return 2 ** (int(integerPart) + 1)


# ((2, 3), (2, 1), (5, 2)),
# ((2, 3), (2, 1), (5, 2)),                                                                                ((4, 4), (4, 4), (4, 4)), 
# ((2, 1), (2, 0), (2, 1)), ((2, 3), (5, 2), (5, 2)),                                                      ((4, 4), (4, 4), (4, 4)), ((10000000000, 0), (10000000000, 0), (0, 0)),
# ((2, 0), (2, 0), (2, 0)), ((2, 1), (2, 1), (2, 1)), ((5, 2), (5, 2), (5, 2)), ((2, 3), (2, 3), (2, 3)), ((4, 4), (4, 4), (4, 4)), ((10000000000, 0), (10000000000, 0), (0, 0)), ((10000000000, 0), (10000000000, 0), (0, 0)), ((10000000000, 0), (10000000000, 0), (0, 0))]

# |               1               |
# |       2       |       3       |
# |   4   |   5   |   6   |   7   |
# | 8 | 9 | 0 | 1 | 2 | 3 | 4 | 5 | <- 0~7に対応
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

    def max_right(self, l, is_ok: "function"):
        # print("---", l)
        l += self.offset
        ll = l // (l & -l) # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
        ans = self.monoid
        # print("#", ll)
        # print(self.tree)
        # print(is_ok(self.func(ans, self.tree[ll])))
        while is_ok(self.func(ans, self.tree[ll])): # そのセグメントが条件を満たすかどうかの判定
            # print("#", ll)
            ans = self.func(ans, self.tree[ll])
            ll += 1
            while ~ll & 1: # llの反転 ~ll = -(ll+1)
                ll >>= 1 # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
            if ll == 1: # 最上層まで到達したら全範囲満たすということ。 → (2べきになるようにモノイド埋めする前の)実際の長さを返す。
                return self.actualLen
        # print(ll, "self.offset", self.offset)
        while ll < self.offset:
            ll <<= 1 # 一階層下のセグメントへ移動 (=2倍)
            # print(">", ll)
            # print(ans, self.tree[ll], self.func(ans, self.tree[ll]))
            # print(is_ok(self.func(ans, self.tree[ll])))
            if is_ok(self.func(ans, self.tree[ll])): # 条件を満たすなら同一階層の隣のセグメントの下層へ。満たさないならそのまま下層へ。
                ans = self.func(ans, self.tree[ll])
                ll += 1
        # print("!", ll)
        return ll - self.offset
  
def main():
    N = int(input())
    A = list(map(int, input().split()))

    def f(x, y):
        if x[0][0] < y[0][0]:
            m1 = x[0]
            if m1 == x[1]:
                if y[0][0] == 10 ** 10:
                    m2 = x[1]
                else:
                    m2 = y[0]
            else:
                if x[1][0] < y[0][0]:
                    m2 = x[1]
                else:
                    m2 = y[0]
        else:
            m1 = y[0]
            if m1 == y[1]:
                if x[0][0] == 10 ** 10:
                    m2 = y[1]
                else:
                    m2 = x[0]
            else:
                if y[1][0] < x[0][0]:
                    m2 = y[1]
                else:
                    m2 = x[0]
        if x[2][0] > y[2][0]:
            M = x[2]
        else:
            M = y[2]
        return (m1, m2, M)
    
    seg = SegTree(((10 ** 10, 0), (10 ** 10, 0), (0, 0)), [((aa, i), (aa, i), (aa, i)) for i, aa in enumerate(A)], f, convertLengthToThePowerOf2=True)
    # print(seg.tree)

    ans = 0
    for l in range(N):
        num = seg.max_right(l,lambda x:x[2][0]<=x[0][0]+x[1][0]) - l - 1
        # print(num)
        ans += num
        # print("---")
    print(ans)

    # for l in range(N):
    #     print(seg.max_right(l,lambda x:x[2]<=x[0]+x[1]))
    return

if __name__ == '__main__':
    main()
