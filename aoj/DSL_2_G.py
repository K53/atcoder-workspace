#! /usr/bin/env python
import sys
INF = 10 ** 9
class LazySegTree:
    unit = 0
    unit_lazy = 0

    @classmethod
    def lazy_propagate_downward(cls, org, late): # 遅延配列内での伝播処理(遅延している更新同士の扱い)
        if org is None: org = cls.unit_lazy
        return org + late

    @classmethod
    def operation(cls, org, late, width): # 遅延配列→値配列への伝播処理(処理を実際にどうするのか)
        """
        width: セル幅(加算クエリなどセルの個数に依存する場合に使用)
        """
        if org is None: org = cls.unit_lazy
        return org + late * width

    @classmethod
    def value_propagate_upward(cls, left, right): # 値配列内での遡上処理(より大きいセグメントへの伝播)
        return left + right

    def __init__(self, bottomList: "list[int]", isLogging: bool = False, convertLengthToThePowerOf2: bool = False):
        # print("index0 は使用されない。常にdefault値")
        self.bottomLen = self._getSegLenOfThePowerOf2(len(bottomList)) if convertLengthToThePowerOf2 else len(bottomList)
        self.actualLen = len(bottomList)
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.value = [self.unit] * self.segLen
        self.width = [1] * self.segLen
        self.lazy = [None] * self.segLen
        self.isLogging = isLogging
        if self.isLogging:
            self.logvalue = [len(str(self.unit)) + 2] * self.segLen
            self.loglazy = [6] * self.segLen # lazyは初期値Noneのため
        self._build(bottomList)

    def _build(self, seq):
        """
        初期化
        O(self.segLen)
        """
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.value[i] = x
            self.lazy[i] = x

        for i in range(self.offset - 1, 0, -1):
            self.width[i] = self.width[i << 1] + self.width[i << 1 | 1]
            self.value[i] = self.value_propagate_upward(self.value[i << 1], self.value[i << 1 | 1])

        # ビルド
        if self.isLogging:
            for i, x in enumerate(seq, self.offset):
                self.logvalue[i] = len(str(x)) + 2
                self.loglazy[i] = len(str(x)) + 2
            for i in range(self.offset - 1, 0, -1):
                self.logvalue[i] = self.logvalue[i << 1] + self.logvalue[i << 1 | 1] + 1
                self.loglazy[i] = self.loglazy[i << 1] + self.loglazy[i << 1 | 1] + 1

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

    def _propagateAt(self, idx: int):
        if self.lazy[idx] is None:
            return
        # 下層の遅延配列に伝播
        self.lazy[idx << 1] = self.lazy_propagate_downward(self.lazy[idx << 1], self.lazy[idx])
        self.lazy[idx << 1 | 1] = self.lazy_propagate_downward(self.lazy[idx << 1 | 1], self.lazy[idx])

        # 値配列側に反映
        self.value[idx << 1] = self.operation(self.value[idx << 1], self.lazy[idx], self.width[idx << 1])
        self.value[idx << 1 | 1] = self.operation(self.value[idx << 1 | 1], self.lazy[idx], self.width[idx << 1 | 1])

        # 評価終了。初期化。
        self.lazy[idx] = None
        return
    
    def rangeUpdate(self, l: int, r: int, x: int):
        if r == l:
            raise Exception("you need to direct [l, r). (l != r)")
        l += self.offset
        r += self.offset

        related_indices = list(self._gindex(l, r))
        # 1) 更新区間に関係するlazyを全て子に伝播させる。
        for i in reversed(related_indices):
            self._propagateAt(i)
        
        # 2) 値の更新区間への処理
        cellWidth = 1 # 各セグメントの傘下の要素数
        while l < r:
            if l & 1: # 奇数(=右側のセグメント)なら配列を更新、右の部屋に行って(+1)から上層へ(>>1)。
                self.lazy[l] = self.lazy_propagate_downward(self.lazy[l], x)
                self.value[l] = self.operation(self.value[l], x, self.width[l])
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = self.lazy_propagate_downward(self.lazy[r], x)
                self.value[r] = self.operation(self.value[r], x, self.width[r])
            l >>= 1
            r >>= 1
            cellWidth <<= 1

        # 3) 値配列の更新
        for i in related_indices:
            self.value[i] = self.value_propagate_upward(self.value[i << 1], self.value[i << 1 | 1])

    def getPoint(self, idx: int):
        """
        一点取得
        O(1)
        """
        idx += self.offset
        related_indices = list(self._gindex(idx, idx + 1))
        # 更新区間に関係するlazyを全て子に伝播させる。
        for i in reversed(related_indices):
            self._propagateAt(i)
        
        return self.value[idx]

    def getRange(self, l: int, r: int):
        l += self.offset
        r += self.offset
        related_indices = list(self._gindex(l, r))
        # 更新区間に関係するlazyを全て子に伝播させる。
        for i in reversed(related_indices):
            self._propagateAt(i)

        vL = self.unit
        vR = self.unit
        while l < r:
            if l & 1:
                vL = self.value_propagate_upward(vL, self.value[l])
                l += 1
            if r & 1:
                r -= 1
                vR = self.value_propagate_upward(self.value[r], vR)
            l >>= 1
            r >>= 1
        return self.value_propagate_upward(vL, vR)

    def _gindex(self, l, r):
        """
        区間[l, r)の値を算出するのに必要なlazyの区間を降順(ボトムアップ)で返す。
        """
        if l < self.offset or r < self.offset:
            raise Exception("need to add offset")
        lm = (l // (l & -l)) >> 1   # lから遡上していき、右側に位置するまで進む。右側に位置したセグメントの1つ上を新たにlとして更新し、そこまでは伝播必要といえる。
        rm = (r // (r & -r)) >> 1   # lから遡上していき、右側に位置するまで進む。右側に位置したセグメントの1つ上を新たにrとして更新し、そこまでは伝播必要といえる。
        while l < r:
            if r <= rm:
                yield r
            if l <= lm:
                yield l
            l >>= 1
            r >>= 1
        while l:
            yield l
            l >>= 1

    def __str__(self) -> str:
        if not self.isLogging:
            return "[" + ", ".join([str(i) for i in self.value]) + "]"
        
        res = ["---------------------\nTree:"]
        PowerOf2Set = set([2 ** i for i in range(8)]) # どうぜログ出力で確認できるのはせいぜいこの辺まで
        for i in range(1, self.segLen):
            if i in PowerOf2Set:
                res.append("\n|")
            res.append(str(self.value[i]).center(self.logvalue[i], " "))
            res.append("|")
        res.append("\nLazy:")
        for i in range(1, self.segLen):
            if i in PowerOf2Set:
                res.append("\n|")
            res.append(str(self.lazy[i]).center(self.loglazy[i], " "))
            res.append("|")
        return "".join(res)

def main():
    N, Q = map(int, input().split())

    seg = LazySegTree([0] * N, True)
    for _ in range(Q):
        t, *args = map(int, input().split())
        if t == 0:
            seg.rangeUpdate(args[0] - 1, args[1], args[2])
        else:
            print(seg.getRange(args[0] - 1, args[1]))

if __name__ == "__main__":
    main()
