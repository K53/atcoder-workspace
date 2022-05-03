#!/usr/bin/env python3

# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E
# AC済み

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 2べきでなくてもいい
class LazySegTree:
    monoid = 0
    monoidForLazy = 0

    @classmethod
    def X_f(cls, x, y):
        return x + y

    def __init__(self, N):
        self.bottomLen = N
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [self.monoid] * self.segLen
        self.lazy = [self.monoidForLazy] * self.segLen

    def build(self, seq):
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.X_f(self.tree[i << 1], self.tree[i << 1 | 1])
            print(self.tree)

    def _eval_at(self, i):
        return self.tree[i] + self.lazy[i] # 評価待ち用の木からセグ木側に反映

    def _propagate_above(self, i):
        H = i.bit_length() - 1 # 対象の要素の上に属する全ての要素について評価と伝播を実施。
        # 頂点側から実行(下に行くほど評価遅延しているので当然上から実施)
        for h in range(H, 0, -1):
            target = i >> h
            self.tree[target] = self._eval_at(target) # 評価待ちの演算を実施
            # 対象ノードの子要素(左右)に対して評価待ち用の木を更新。
            self.lazy[target << 1] += self.lazy[target]
            self.lazy[target << 1 | 1] += self.lazy[target]
            self.lazy[target] = self.monoidForLazy # 対象の評価待ちは無くなったのでクリア。
        return

    def fold(self, l: int, r: int):
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
                vL += self._eval_at(l)
                l += 1
            if r & 1:
                r -= 1
                vR += self._eval_at(r)
            l >>= 1
            r >>= 1
        return self.X_f(vL, vR)

    def operate_range(self, l, r, x):
        l += self.offset
        r += self.offset
        while l < r:
            if l & 1:
                self.lazy[l] += x
                l += 1
            if r & 1:
                r -= 1
                self.lazy[r] += x
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
            # print(seg.lazy)
            # print()
        else:
            x = query[1]
            print(seg.fold(x - 1, x))
    return

if __name__ == '__main__':
    main()
