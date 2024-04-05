#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

class SegTree:
    def __init__(self, unit: int, bottomList: "list[int]", func: "function", isLogging: bool = False, convertLengthToThePowerOf2: bool = False):
        self.unit = unit
        self.func = func
        self.bottomLen = self._getSegLenOfThePowerOf2(len(bottomList)) if convertLengthToThePowerOf2 else len(bottomList)
        self.actualLen = len(bottomList)
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [unit] * self.segLen
        self.isLogging = isLogging
        if self.isLogging:
            self.logtree = [len(str(unit)) + 2] * self.segLen
        self._build(bottomList)

    def _build(self, seq):
        """
        初期化
        O(self.segLen)
        """
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
            if self.isLogging:
                self.logtree[i] = len(str(x)) + 2
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])
            if self.isLogging:
                self.logtree[i] = max(len(str(self.tree[i])) + 2, self.logtree[i << 1] + self.logtree[i << 1 | 1] + 1)

    def _getSegLenOfThePowerOf2(self, ln: int):
        """
        直近の2べきの長さを算出
        """
        if ln <= 0:
            return 1
        else:    
            import math
            decimalPart, integerPart = math.modf(math.log2(ln))
            return 2 ** (int(integerPart) + (0 if decimalPart == float(0) else 1))

    def pointAdd(self, i: int, val: int):
        """
        一点加算 他演算
        O(log(self.bottomLen))
        """
        i += self.offset
        self.tree[i] += val
        if self.isLogging:
            self.logtree[i] = len(str(self.tree[i])) + 2
        # self.tree[i] = self.func(self.tree[i], val) <- こっちの方が都度の修正は発生しない。再帰が遅くないか次第。
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子
            if self.isLogging:
                self.logtree[i] = max(len(str(self.tree[i])) + 2, self.logtree[i << 1] + self.logtree[i << 1 | 1] + 1)

    def pointUpdate(self, i: int, val: int):
        """
        一点更新
        O(log(self.bottomLen))
        """
        i += self.offset
        self.tree[i] = val
        if self.isLogging:
            self.logtree[i] = len(str(self.tree[i])) + 2
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子
            if self.isLogging:
                self.logtree[i] = max(len(str(self.tree[i])) + 2, self.logtree[i << 1] + self.logtree[i << 1 | 1] + 1)

    def getRange(self, l: int, r: int):
        """
        区間取得 (l ≦ X < r)
        l ~ r-1までの区間 (0-indexed)。※右端を含まない。
        O(log(self.bottomLen))
        """
        l += self.offset
        r += self.offset
        vL = self.unit
        vR = self.unit
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

    def getPoint(self, i: int):
        """
        一点取得
        O(1)
        """
        i += self.offset
        return self.tree[i]

    def max_right(self, l, is_ok: "function"):
        """
        二分探索
        O(log(self.bottomLen))
        ※ セグ木上の二分探索をする場合は2べきにすること。
        # !!!! ng側が返却される !!!!!
        """
        print("セグ木上の二分探索をする場合は2べきにすること。 convertLengthToThePowerOf2=True")
        l += self.offset
        idx = l // (l & -l) # lから始まる最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
        ans = self.unit
        while is_ok(self.func(ans, self.tree[idx])): # そのセグメントが条件を満たすかどうかの判定
            # 条件を満たす限り上へとより範囲を広げていく。
            ans = self.func(ans, self.tree[idx])
            idx += 1
            idx //= (idx & -idx) 
            if idx == 1: # 最上層まで到達したら全範囲満たすということ。 → (2べきになるようにモノイド埋めする前の)実際の長さを返す。
                return self.actualLen
        while idx < self.offset:
            # 下へと降りていき境界値を見つける。
            idx <<= 1 # 一階層下のセグメント(左側)へ移動 (=2倍)
            #
            # |           idx           |
            # |   idx<<1   | idx<<1 + 1 |
            #
            if is_ok(self.func(ans, self.tree[idx])): # 条件を満たすなら同一階層の右側のセグメントの下層(左側)へ。満たさないならそのまま下層(左側)へ。
                ans = self.func(ans, self.tree[idx])
                idx += 1
        return idx - self.offset - 1

    # 未検証
    def min_left(self, r, is_ok):
        r += self.offset
        rr = max(r // (~r & -~r), 1)
        ans = self.unit
        while is_ok(self.func(self.tree[rr], ans)):
            ans = self.func(self.tree[rr], ans)
            rr -= 1
            while rr & 1:
                rr >>= 1
            if rr == 0:
                return -1
        while rr < self.offset:
            rr <<= 1
            if is_ok(self.func(self.tree[rr+1], ans)):
                ans = self.func(self.tree[rr+1], ans)
            else:
                rr += 1
        return rr - self.offset

    def __str__(self) -> str:
        if not self.isLogging:
            return "[" + ", ".join([str(i) for i in self.tree]) + "]"
        
        res = []
        PowerOf2Set = set([2 ** i for i in range(8)]) # どうぜログ出力で確認できるのはせいぜいこの辺まで
        for i in range(1, self.segLen):
            if i in PowerOf2Set:
                res.append("\n|")
            res.append(str(self.tree[i]).center(self.logtree[i], " "))
            res.append("|")
        return "".join(res)

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    def f(a, b):
        if a[0] < b[0]:
            return a
        return b
    INF = 10 ** 9
    seg = SegTree(unit=(INF, -1), bottomList=[(A[i], i) for i in range(N)], func=f, isLogging=True)
    for _ in range(Q):
        t, *args = map(int, input().split())
        if t == 1:
            l, r = args[0] - 1, args[1] - 1
            al, ar = seg.getPoint(l)[0], seg.getPoint(r)[0]
            seg.pointUpdate(l, (ar, l))
            seg.pointUpdate(r, (al, r))
        else:
            l, r = args[0] - 1, args[1] - 1
            print(seg.getRange(l, r + 1)[1] + 1)
    return
        
if __name__ == '__main__':
    main()