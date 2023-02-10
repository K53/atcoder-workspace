#!/usr/bin/env python3
import sys
# from functools import cmp_to_key
input = lambda: sys.stdin.readline().strip()

def main():
    N, Q = map(int, input().split())
    c = list(map(int, input().split()))
    
    class SegTree:
        def __init__(self):
            # print("index0 は使用されない。常にdefault値")
            self.monoid = 0
            self.bottomLen = N
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [self.monoid] * self.segLen
            for i in range(self.offset - 1, 0, -1):
                self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

        def pointAdd(self, i: int, val: int):
            i += self.offset
            self.tree[i] += val
            # self.tree[i] = self.func(self.tree[i], val) <- こっちの方が都度の修正は発生しない。再帰が遅くないか次第。
            while i > 1:
                i >>= 1 # 2で割って頂点に達するまで下層から遡上
                self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1] # 必ず末尾0と1がペアになるのでor演算子

        def getRange(self, l: int, r: int):
            l += self.offset
            r += self.offset
            vL = self.monoid
            vR = self.monoid
            while l < r:
                if l & 1:
                    vL += self.tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    vR += self.tree[r]
                l >>= 1
                r >>= 1
            return vL + vR

    ans = [0] * Q
    lr = [(i, *map(int, input().split())) for i in range(Q)]
    lr.sort(key=lambda query: query[2])
    color_to_latest_idx = [-1] * (N + 1)

    tot = len(set(c))
    unappear = tot
    seg = SegTree()
    prev_rr = 0
    for idx, ll, rr in lr:
        ll -= 1
        # print(">", rr, ll, idx)
        if rr != prev_rr:
            for dr in range(prev_rr, rr):
                # print(dr)
                if color_to_latest_idx[c[dr]] == -1:
                    unappear -= 1
                else:
                    seg.pointAdd(color_to_latest_idx[c[dr]], -1)
                color_to_latest_idx[c[dr]] = dr
                seg.pointAdd(dr, 1)
        # print(tot, "-", seg.getRange(0, ll) - unappear)
        ans[idx] = tot - seg.getRange(0, ll) - unappear
        prev_rr = rr
    
    print(*ans, sep="\n")
        
        
    
    # Mo's Algorithm ============= TLE解
    # sq = Q ** 0.5
    # # aがbよりも前に置くなら-1、後ろに置くなら1
    # @cmp_to_key
    # def _f(a, b):
    #     if a[0]//sq != b[0]//sq:
    #         if a[0] > b[0]: return 1
    #         if a[0] < b[0]: return -1
    #         return 0
    #     else:
    #         if a[0]//sq % 2 == 0:
    #             if a[1] > b[1]: return 1
    #             if a[1] < b[1]: return -1
    #             return 0
    #         else:
    #             if a[1] > b[1]: return -1
    #             if a[1] < b[1]: return 1
    #             return 0
        
    # lr = sorted([(l[i] - 1, r[i], i) for i in range(Q)], key=_f)
    # # print(lr)

    # total_kinds = 0
    # each_count = [0] * (N + 1)
    # def _add(k):
    #     nonlocal total_kinds
    #     if each_count[k] == 0:
    #         total_kinds += 1
    #     each_count[k] += 1
    
    # def _del(k):
    #     nonlocal total_kinds
    #     each_count[k] -= 1
    #     if each_count[k] == 0:
    #         total_kinds -= 1

    # ans = [-1] * Q
    # cur_l, cur_r = 0, 0
    # for i in range(Q):
    #     ll, rr, idx = lr[i]
    #     # print(i, "---", cur_l, ll, cur_r, rr)
    #     while cur_l > ll:
    #         cur_l -= 1
    #         _add(c[cur_l]) # 移動先を足す
    #     while cur_l < ll:
    #         _del(c[cur_l]) # 移動元を引く
    #         cur_l += 1
    #     while cur_r > rr:
    #         cur_r -= 1
    #         _del(c[cur_r]) # 移動先を引く
    #     while cur_r < rr:
    #         _add(c[cur_r]) # 移動元を足す
    #         cur_r += 1
    #     ans[idx] = total_kinds
    # print(*ans, sep="\n")
    ## ==============================================


    return

if __name__ == '__main__':
    main()
