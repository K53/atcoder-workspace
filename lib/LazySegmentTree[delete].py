# ------------------------------------------------------------------------------
#     遅延セグメント木 (1-indexed)
# ------------------------------------------------------------------------------
# 解説
# 
#
# リンク
# - https://tsutaj.hatenablog.com/entry/2017/03/30/224339
# 
# 計算量
# 
# verify
# - 
# ------------------------------------------------------------------------------
class LazySegmentTree:
    pass



# ---------------------------------------------------------------
# 遅延セグメント木 (区間加算用)
# Python/pypy系は再帰が遅いので場合によっては展開してインラインに書く必要あり
#
#
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E&lang=ja
# ---------------------------------------------------------------


#!/usr/bin/env python3
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 2べきでなくてもいい
class LazySegTree:
    monoid = 0
    monoidForOperation = 0

    @classmethod
    def X_f(cls, x, y):
        return x + y

    @classmethod
    def A_f(cls, x, y):
        return x + y

    @classmethod
    def operate(cls, x, y):
        return x + y

    def __init__(self, N):
        self.bottomLen = N
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [self.monoid] * self.segLen
        self.operationTree = [self.monoidForOperation] * self.segLen

    def build(self, seq):
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.X_f(self.tree[i << 1], self.tree[i << 1 | 1])
            print(self.tree)

    def _eval_at(self, i):
        return self.operate(self.tree[i], self.operationTree[i]) # 評価待ち用の木からセグ木側に反映

    def _propagate_at(self, i):
        self.tree[i] = self._eval_at(i) # 評価待ちの演算を実施
        # 対象ノードの子要素(左右)に対して評価待ち用の木を更新。
        self.operationTree[i << 1] = self.A_f(self.operationTree[i << 1], self.operationTree[i]) 
        self.operationTree[i << 1 | 1] = self.A_f(self.operationTree[i << 1 | 1], self.operationTree[i])
        self.operationTree[i] = self.monoidForOperation # 対象の評価待ちは無くなったのでクリア。

    def _propagate_above(self, i):
        H = i.bit_length() - 1 # 対象の要素の上に属する全ての要素について評価と伝播を実施。
        # 頂点側から実行(下に行くほど評価遅延しているので当然上から実施)
        for h in range(H, 0, -1):
            self._propagate_at(i >> h) # 評価の伝播
        return

    def _recalc_above(self, i):
        while i > 1:
            i >>= 1
            self.tree[i] = self.X_f(self._eval_at(i << 1), self._eval_at(i << 1 | 1))
        return

    def fold(self, l, r):
        l += self.offset
        r += self.offset
        L0 = l // (l & -l) # 奇数になるまでLを2で割ったもの
        R0 = r // (r & -r) - 1 # 奇数になるまでRを2で割ったもの
        self._propagate_above(L0)
        self._propagate_above(R0)
        vL = self.monoid
        vR = self.monoid
        while l < r:
            if l & 1:
                vL = self.X_f(vL, self._eval_at(l))
                l += 1
            if r & 1:
                r -= 1
                vR = self.X_f(self._eval_at(r), vR)
            l >>= 1
            r >>= 1
        return self.X_f(vL, vR)

    def operate_range(self, l, r, x):
        l += self.offset
        r += self.offset
        while l < r:
            if l & 1:
                self.operationTree[l] = self.A_f(self.operationTree[l], x)
                l += 1
            if r & 1:
                r -= 1
                self.operationTree[r] = self.A_f(self.operationTree[r], x)
            l >>= 1
            r >>= 1


def main():
    N, Q = map(int, readline().split())
    seg = LazySegTree(N + 1)
    # print(seg.tree)
    for _ in range(Q):
        query = list(map(int, readline().split()))
        if query[0] == 0:
            s, t, x = query[1], query[2], query[3]
            seg.operate_range(s - 1, t - 1 + 1, x)
            # print(seg.tree)
            # print(seg.operationTree)
            # print()
        else:
            x = query[1]
            print(seg.fold(x - 1, x))
    return

if __name__ == '__main__':
    main()
