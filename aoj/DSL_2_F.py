#! /usr/bin/env python
import sys
class LazySegTree:

    @classmethod
    def opeA(cls, org, late): # 遅延配列内での伝播処理(遅延している更新同士の扱い)
        return late

    @classmethod
    def opeB(cls, org, late): # 遅延配列→値配列への伝播処理(処理を実際にどうするのか)
        return late

    @classmethod
    def calc(clas, org, late): # 値配列内での遡上処理(より大きいセグメントへの伝播)
        return min(org, late)

    def __init__(self, unit: int, bottomList: "list[int]", func: "function", updateFunc: "function", propagateFunc: "function", isLogging: bool = False, convertLengthToThePowerOf2: bool = False):
        # print("index0 は使用されない。常にdefault値")
        self.unit = unit
        # self.func = func
        # self.updateFunc = updateFunc
        # self.propagateFunc = propagateFunc
        self.bottomLen = self._getSegLenOfThePowerOf2(len(bottomList)) if convertLengthToThePowerOf2 else len(bottomList)
        self.actualLen = len(bottomList)
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.segDepth = (self.segLen - 1).bit_length()
        self.value = [unit] * self.segLen
        self.lazy = [None] * self.segLen
        self.isLogging = isLogging
        if self.isLogging:
            self.logvalue = [len(str(unit)) + 2] * self.segLen
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
        # # 値配列側に反映
        self.value[idx << 1] = self.opeB(self.value[idx << 1], self.lazy[idx])
        self.value[idx << 1 | 1] = self.opeB(self.value[idx << 1 | 1], self.lazy[idx])

        # 現在の評価対象が最下層でないなら下層の遅延配列に伝播
        self.lazy[idx << 1] = self.opeA(self.lazy[idx << 1], self.lazy[idx])
        self.lazy[idx << 1 | 1] = self.opeA(self.lazy[idx << 1 | 1], self.lazy[idx])

        # 評価終了。初期化。
        self.lazy[idx] = None
        return
    
    def rangeUpdate(self, l: int, r: int, x: int):
        if r == l:
            raise Exception("you need to direct [l, r). (l != r)")
        l += self.offset
        r += self.offset

        related_indices = list(self._gindex(l, r))
        # 更新区間に関係するlazyを全て子に伝播させる。
        for idx in reversed(related_indices):
            self._propagateAt(idx)
        
        # 値の更新区間への処理
        cellWidth = 1 # 各セグメントの傘下の要素数
        while l < r:
            if l & 1: # 奇数(=右側のセグメント)なら配列を更新、右の部屋に行って(+1)から上層へ(>>1)。
                self.lazy[l] = self.opeA(self.lazy[l], x)
                self.value[l] = self.opeB(self.value[l], x)
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] = self.opeA(self.lazy[r], x)
                self.value[r] = self.opeB(self.value[r], x)
            l >>= 1
            r >>= 1
            cellWidth <<= 1
        
        for idx in related_indices:
            self.value[idx] = self.calc(self.value[idx << 1], self.value[idx << 1 | 1])

    def getRange(self, l: int, r: int):
        l += self.offset
        r += self.offset
        related_indices = list(self._gindex(l, r))
        # 更新区間に関係するlazyを全て子に伝播させる。
        for idx in reversed(related_indices):
            self._propagateAt(idx)

        vL = self.unit
        vR = self.unit
        while l < r:
            if l & 1:
                vL = self.calc(vL, self.value[l])
                l += 1
            if r & 1:
                r -= 1
                vR = self.calc(self.value[r], vR)
            l >>= 1
            r >>= 1
        return self.calc(vL, vR)

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
        
        res = ["Tree:"]
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
    INF = 2 ** 31 - 1

    def updateFunc(org, late):
        if org is None:
            return late
        return org + late

    def propageteFunc(org, late):
        if org is None:
            return late // 2
        return org + late // 2
    
    seg = LazySegTree(INF, [INF] * N, min, updateFunc, propageteFunc, True, True)
    for _ in range(Q):
        t, *args = map(int, input().split())
        if t == 0:
            seg.rangeUpdate(args[0], args[1] + 1, args[2])
        else:
            print(seg.getRange(args[0], args[1] + 1))

if __name__ == "__main__":
    main()
