#!/usr/bin/env python3
import sys
import heapq
from collections import defaultdict
INF = 10 ** 16
class HeapDictMax:
    def __init__(self):
        self.q=[]
        self.d=defaultdict(int)

    def insert(self, x):
        """要素xの挿入"""
        heapq.heappush(self.q, -x)
        self.d[-x] += 1

    def erase(self, x):
        """要素xの削除"""
        if self.d[-x] == 0:
            print(-x, " is not in HeapDict")
            return
        else:
            self.d[-x] -= 1

        # 先頭から論理削除済みのものを物理削除する
        while len(self.q) != 0:
            if self.d[self.q[0]] == 0:
                heapq.heappop(self.q)
            else:
                break
    
    def isEmpty(self):
        """O(1)。キューが空かどうか。"""
        return len(self.q) != 0
    
    def size(self):
        """O(過去に出現した要素の種類n) : キューが空かどうかのみ知りたい場合はisEmpty()使用推奨"""
        return sum(self.d.values())

    def exist(self, x):
        """O(1)。要素の存在確認"""
        return self.d[-x] != 0
    
    def getExistList(self):
        """O(len(self.q))。キュー内の実際に存在する要素のみを返す(遅延削除のため、self.qだと削除済みでも残っている要素が表示される)"""
        return [-i for i in self.q if self.exist(-i)]

    def dryPop(self):
        """O(1)。先頭要素(通常は最小値)を返す。キューが空ならNoneを返す"""
        return -self.q[0] if self.isEmpty() else INF

    def __str__(self):
        """O(len(self.q))。先頭要素取得に影響しない要素は遅延削除のため、キュー内に存在しているが事実上削除済みのものは括弧()書きしている"""
        return "[" + ", ".join([str(-i) if self.exist(-i) else "({})".format(-i) for i in self.q]) + "]"

class SegTree:
    def __init__(self, monoid: int, bottomList: "list[int]", func: "function", convertLengthToThePowerOf2: bool = False):
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
        self._build(bottomList)

    """
    初期化
    O(self.segLen)
    """
    def _build(self, seq):
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
    区間取得 (l ≦ X < r)
    l ~ r-1までの区間 (0-indexed)。※右端を含まない。
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
    O(1)
    """
    def getPoint(self, i: int):
        i += self.offset
        return self.tree[i]

    """
    二分探索
    O(log(self.bottomLen))
    ※ セグ木上の二分探索をする場合は2べきにすること。
    # !!!! ng側が返却される !!!!!
    """
    def max_right(self, l, is_ok: "function"):
        print("セグ木上の二分探索をする場合は2べきにすること。")
        l += self.offset
        ll = l // (l & -l) # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
        ans = self.monoid
        while is_ok(self.func(ans, self.tree[ll])): # そのセグメントが条件を満たすかどうかの判定
            ans = self.func(ans, self.tree[ll])
            ll += 1
            while ~ll & 1: # llの反転 ~ll = -(ll+1)
                ll >>= 1 # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
            if ll == 1: # 最上層まで到達したら全範囲満たすということ。 → (2べきになるようにモノイド埋めする前の)実際の長さを返す。
                return self.actualLen
        while ll < self.offset:
            ll <<= 1 # 一階層下のセグメントへ移動 (=2倍)
            if is_ok(self.func(ans, self.tree[ll])): # 条件を満たすなら同一階層の隣のセグメントの下層へ。満たさないならそのまま下層へ。
                ans = self.func(ans, self.tree[ll])
                ll += 1
        return ll - self.offset # ng側が返る

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

def solve(N: int, Q: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    LK = 2 * 10 ** 5 + 1
    l = [HeapDictMax() for _ in range(LK)]
    where = [-1] * N
    INF = 10 ** 16
    for i in range(N):
        where[i] = B[i] - 1
        l[B[i] - 1].insert(A[i])
    base = [l[i].dryPop() for i in range(LK)]
    seg = SegTree(INF, base, min)
    for cc, dd in zip(C, D):
        kin = where[cc - 1]
        l[kin].erase(A[cc - 1])
        l[dd - 1].insert(A[cc - 1])
        where[cc - 1] = dd - 1
        old = l[kin].dryPop()
        new = l[dd - 1].dryPop()
        seg.pointUpdate(kin, old)
        seg.pointUpdate(dd - 1, new)
        print(seg.getRange(0, LK))
    
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, Q, A, B, C, D)

if __name__ == '__main__':
    main()
