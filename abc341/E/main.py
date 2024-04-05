#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str

class SegTree:
    def __init__(self, monoid: int, bottomList: "list[int]", func: "function", isLogging: bool = False, convertLengthToThePowerOf2: bool = False):
        # print("index0 は使用されない。常にdefault値")
        self.monoid = monoid
        self.func = func
        self.bottomLen = self._getSegLenOfThePowerOf2(len(bottomList)) if convertLengthToThePowerOf2 else len(bottomList)
        self.actualLen = len(bottomList)
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen
        self.isLogging = isLogging
        if self.isLogging:
            self.logtree = [len(str(monoid)) + 2] * self.segLen
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
        if r == -1:
            r = self.offset
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

    def getPoint(self, i: int):
        """
        一点取得
        O(1)
        """
        if i == -1:
            i = self.offset
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
        ans = self.monoid
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
        ans = self.monoid
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

# Generated by 2.13.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, Q = map(int, input().split())
    S = input()
    A = [1 if S[i] != S[i + 1] else 0 for i in range(N - 1)]
    def add(a, b):
        return a + b
    seg = SegTree(0, A, add)
    for _ in range(Q):
        t, l, r = map(int, input().split())
        l -= 1
        r -= 1
        if t == 1:
            if l != 0:
                seg.pointUpdate(l - 1, seg.getPoint(l - 1) ^ 1)
            if r != N - 1:
                seg.pointUpdate(r, seg.getPoint(r) ^ 1)
        else:
            c = seg.getRange(l, r)
            print(YES if c == r - l else NO)
    
if __name__ == '__main__':
    main()
