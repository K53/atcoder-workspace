#!/usr/bin/env python3
def main():
    from sys import stdin
    INF = 10 ** 9
    class LazySegTree:
        def __init__(self, bottomList: "list[int]"):
            self.bottomLen = len(bottomList)
            self.actualLen = len(bottomList)
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.value = [0] * self.segLen
            self.width = [1] * self.segLen
            self.lazy = [None] * self.segLen
            
            for i, x in enumerate(bottomList, self.offset):
                self.value[i] = x
                self.lazy[i] = x

            for i in range(self.offset - 1, 0, -1):
                self.width[i] = self.width[i << 1] + self.width[i << 1 | 1]
                self.value[i] = self.value[i << 1] + self.value[i << 1 | 1]

        def _propagateAt(self, idx: int):
            if self.lazy[idx] is None:
                return
            # 下層の遅延配列に伝播
            self.lazy[idx << 1] = self.lazy[idx] if self.lazy[idx << 1] is None else self.lazy[idx << 1] + self.lazy[idx]
            self.lazy[idx << 1 | 1] = self.lazy[idx] if self.lazy[idx << 1 | 1] is None else self.lazy[idx << 1 | 1] + self.lazy[idx]

            
            # 値配列側に反映
            self.value[idx << 1] = self.lazy[idx] * self.width[idx << 1] if self.value[idx << 1] is None else self.value[idx << 1] + self.lazy[idx] * self.width[idx << 1]
            self.value[idx << 1 | 1] = self.lazy[idx] * self.width[idx << 1 | 1] if self.value[idx << 1 | 1] is None else self.value[idx << 1 | 1] + self.lazy[idx] * self.width[idx << 1 | 1]

            # 評価終了。初期化。
            self.lazy[idx] = None
            return
        
        def rangeUpdate(self, l: int, r: int, x: int):
            if r == -1:
                r = self.offset
            if r == l:
                raise Exception("you need to direct [l, r). (l != r)")
            l += self.offset
            r += self.offset

            related_indices = list(self._gindex(l, r))
            # 1) 更新区間に関係するlazyを全て子に伝播させる。
            for idx in reversed(related_indices):
                if self.lazy[idx] is None:
                    continue
                # 下層の遅延配列に伝播
                self.lazy[idx << 1] = self.lazy[idx] if self.lazy[idx << 1] is None else self.lazy[idx << 1] + self.lazy[idx]
                self.lazy[idx << 1 | 1] = self.lazy[idx] if self.lazy[idx << 1 | 1] is None else self.lazy[idx << 1 | 1] + self.lazy[idx]

                
                # 値配列側に反映
                self.value[idx << 1] = self.lazy[idx] * self.width[idx << 1] if self.value[idx << 1] is None else self.value[idx << 1] + self.lazy[idx] * self.width[idx << 1]
                self.value[idx << 1 | 1] = self.lazy[idx] * self.width[idx << 1 | 1] if self.value[idx << 1 | 1] is None else self.value[idx << 1 | 1] + self.lazy[idx] * self.width[idx << 1 | 1]

                # 評価終了。初期化。
                self.lazy[idx] = None
            
            # 2) 値の更新区間への処理
            cellWidth = 1 # 各セグメントの傘下の要素数
            while l < r:
                if l & 1: # 奇数(=右側のセグメント)なら配列を更新、右の部屋に行って(+1)から上層へ(>>1)。
                    self.lazy[l] = x if self.lazy[l] is None else self.lazy[l] + x
                    self.value[l] = x * self.width[l] if self.value[l] is None else self.value[l] + x * self.width[l]
                    l += 1
                if r & 1:
                    r -= 1
                    self.lazy[r] = x if self.lazy[r] is None else self.lazy[r] + x
                    self.value[r] = x * self.width[r] if self.value[r] is None else self.value[r] + x * self.width[r]
                l >>= 1
                r >>= 1
                cellWidth <<= 1

            # 3) 値配列の更新
            for i in related_indices:
                self.value[i] = self.value[i << 1] + self.value[i << 1 | 1]

        def getPoint(self, kkk: int):
            """
            一点取得
            O(1)
            """
            if kkk == -1:
                kkk = self.offset
            kkk += self.offset
            related_indices = list(self._gindex(kkk, kkk + 1))
            # 更新区間に関係するlazyを全て子に伝播させる。
            for idx in reversed(related_indices):
                if self.lazy[idx] is None:
                    continue
                # 下層の遅延配列に伝播
                self.lazy[idx << 1] = self.lazy[idx] if self.lazy[idx << 1] is None else self.lazy[idx << 1] + self.lazy[idx]
                self.lazy[idx << 1 | 1] = self.lazy[idx] if self.lazy[idx << 1 | 1] is None else self.lazy[idx << 1 | 1] + self.lazy[idx]

                
                # 値配列側に反映
                self.value[idx << 1] = self.lazy[idx] * self.width[idx << 1] if self.value[idx << 1] is None else self.value[idx << 1] + self.lazy[idx] * self.width[idx << 1]
                self.value[idx << 1 | 1] = self.lazy[idx] * self.width[idx << 1 | 1] if self.value[idx << 1 | 1] is None else self.value[idx << 1 | 1] + self.lazy[idx] * self.width[idx << 1 | 1]

                # 評価終了。初期化。
                self.lazy[idx] = None
            
            return self.value[kkk]

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

    readline = stdin.readline
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    B = list(map(int, readline().split()))

    seg = LazySegTree(A)
    for i in range(M):
        idx = B[i]
        count = seg.getPoint(idx)
        seg.rangeUpdate(idx, idx + 1, -count)

        p, q = divmod(count, N)
        if p != 0:
            seg.rangeUpdate(0, N, p)
        if idx + q < N:
            if idx + 1 != idx + q + 1:
                seg.rangeUpdate(idx + 1, idx + q + 1, 1)
        else:
            if idx + 1 != N:
                seg.rangeUpdate(idx + 1, N, 1)
            seg.rangeUpdate(0, ((idx + q) % N) + 1, 1)

    for i in range(N):
        seg._propagateAt(i)
    print(*seg.value[-N:])
    # print(*[seg.getPoint(i) for i in range(N)])

main()