#!/usr/bin/env python3
class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int, func: "function(int, int)"):
        self.initVal = initVal
        self.func = func
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = val # Update # 更新方法も変更が必要な場合は書き換えること。 eg.) XOR演算など |= val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])

    def rangeQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = self.initVal
        while l < r:
            if l % 2 == 1:
                res = self.func(res, self.tree[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                res = self.func(res, self.tree[r - 1])
                r -= 1
            r //= 2
        return res

def main():
    N, Q = map(int, input().split())
    sgl = SegmentTree(0, N, max)
    sgr = SegmentTree(10 ** 10, N, min)
    for i in range(N - 1):
        L, R = map(int, input().split())
        sgl.pointUpdate(i, L)
        sgr.pointUpdate(i, R)

    # ok -- ng
    def is_ok_l(k: int, st: int, border: int):
        print("$$", sgl.rangeQuery(st, k), st, k)
        return sgl.rangeQuery(k, st) <= border   # 条件式

    # ng -- ok
    def is_ok_r(k: int, st: int, border: int):
        # print("$$", sgr.rangeQuery(st, k), st, k)
        # if not k > st or not k <= N:
        #     return False
        return sgr.rangeQuery(st, k) >= border   # 条件式

    def binSearch_l(ng: int, ok: int, st: int, border: int):
        print(ng, ok)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            print("target > ", mid)
            result = is_ok_l(mid, st, border)
            print(result)
            if result:
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            print(ng, ok)          # 半分に切り分ける毎の2値の状態
        return ng 

    def binSearch_r(ok: int, ng: int, st: int, border: int):
        print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            print("target > ", mid)
            result = is_ok_r(mid, st, border)
            print(result)
            if result:
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ng 
        
    for _ in range(Q):
        A, B = map(int, input().split())
        B -= 1
        ll = binSearch_l(-1, B + 1, B, A) + 2 if not B == 0 else 1
        rr = binSearch_r(B - 1, N, B, A) if not B == N - 1 else N - 1
        print(sgl.tree)
        print(sgr.tree)
        print(ll)
        print(rr)
        print("--")
        # return

if __name__ == '__main__':
    main()
