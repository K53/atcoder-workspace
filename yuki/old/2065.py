#!/usr/bin/env python3


class SegTree:
    def __init__(self, monoid, bottomList, func, convertLengthToThePowerOf2: bool = False):
        # print("index0 は使用されない。常にdefault値")
        self.monoid = monoid
        self.func = func
        self.actualLen = len(bottomList)
        self.bottomLen = len(bottomList) if not convertLengthToThePowerOf2 else self.getSegLenOfThePowerOf2(len(bottomList))
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
    """
    一点加算
    O(log(self.bottomLen))
    """
    def pointAdd(self, i: int, val: int):
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

monoid = [0, 0]

# 利用する関数を定義
def add(A: int, B: int):
    return [A[0] + B[0], A[1] + B[1]]

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = [(aa, 100, idx + 1, 0, 0) for idx, aa in enumerate(A)]
    seg = SegTree(monoid, [[0, 0] for _ in range(N)], add)
    for qi in range(Q):
        L, R, X = map(int, input().split())
        queries.append((X, 0, L, R, qi))
    queries.sort()
    ans = [0] * Q
    for num, is_query, cidx_l, cidx_r, qi in queries:
        if is_query == 100:
            # print(cidx_l)
            seg.pointAdd(cidx_l - 1, [num, 1])
            # print(seg.tree)
        else:
            # print(seg.tree)
            tot, k = seg.getRange(cidx_l - 1, cidx_r)
            ideal = cidx_r - cidx_l + 1
            res = (ideal - k) * num + tot
            ans[qi] = res
            # print(ans)

    print(*ans, sep="\n")

if __name__ == '__main__':
    main()