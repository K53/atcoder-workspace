#!/usr/bin/env python3
INF = 10 ** 6
class SegmentTree:
    def __init__(self, monoid: int, bottomLen: int, operation: "function"):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.bottomLen + [[i, monoid]for i in range(self.bottomLen)]
        self.operation = operation
        return
    
    """ 1点取得
    """
    def getPoint(self, index: int):
        segIndex = index + self.offset
        return self.tree[segIndex]
    
    """ 1点更新
    O(1)
    """
    def pointUpdateWithoutRebuild(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = [index, val]          # 各マスの更新方法
        return
    
    """ 全区間更新
    O(bottomLen) # =セグ木の配列長
    """
    def allBuild(self):
        for segIndex in reversed(range(self.offset)):
            if segIndex == 0:
                return
            self.tree[segIndex] = self.operation(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
        return

    """ 1点更新 + リビルド
    O(log(bottomLen))
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = [index, val]          # 各マスの更新方法
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.operation(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
        return

    def rangeQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = [0, self.monoid]                   # クエリの初期値
        while l < r:
            if l % 2 == 1:
                res = self.operation(res, self.tree[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                res = self.operation(res, self.tree[r - 1])
                r -= 1
            r //= 2
        return res

def minWithIndex(a: "list[val, index]", b: "list[val, index]"):
    # print("minWithIndex", a, b)
    return a if a[1] < b[1] else b

# def main(N, Q, A, query):
def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    tr = SegmentTree(monoid=INF, bottomLen=2**18, operation=minWithIndex)
    for i in range(N):
        tr.pointUpdateWithoutRebuild(i, A[i])
    tr.allBuild()
    # print(tr.tree)
    ans = []
    for i in range(Q):
        t, l, r = map(int, input().split())
        # t, l, r = query[i][0], query[i][1], query[i][2]
        if t == 1:
            al, ar = tr.getPoint(l - 1), tr.getPoint(r - 1)
            tr.pointUpdate(l - 1, ar[1])
            tr.pointUpdate(r - 1, al[1])
            # print(tr.tree)
        else:
            i, _ = tr.rangeQuery(l - 1, r)
            print(i + 1)
            ans.append(i + 1)
            # print(tr.tree)
    return ans            


# def ac(N, Q, A, query):
#     #####segfunc#####
#     def segfunc(x, y):
#         if x[0] < y[0]:
#             return x
#         else:
#             return y
#     #################

#     #####単位元#####
#     ide_ele = 2**31-1
#     #################

#     class SegTree:
#         """
#         init(init_val, ide_ele): 配列init_valで初期化 O(N)
#         update(k, x): k番目の値をxに更新 O(logN)
#         query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
#         """
#         def __init__(self, init_val, segfunc, ide_ele):
#             """
#             init_val: 配列の初期値
#             segfunc: 区間にしたい操作
#             ide_ele: 単位元
#             n: 要素数
#             num: n以上の最小の2のべき乗
#             tree: セグメント木(1-index)
#             """
#             n = len(init_val)
#             self.segfunc = segfunc
#             self.ide_ele = ide_ele
#             self.num = 1 << (n - 1).bit_length()
#             self.tree = [[ide_ele, ide_ele] for _ in range(2 * self.num)]
#             # 配列の値を葉にセット
#             for i in range(n):
#                 self.tree[self.num + i] = init_val[i]
#             # 葉からどんどん上へ構築していく
#             for i in range(self.num - 1, 0, -1):
#                 self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])


#         def update(self, k, x):
#             """
#             k番目の値をxに更新.
#             k: index(0-index)
#             x: update value
#             """
#             k += self.num
#             self.tree[k] = x
#             while k > 1:
#                 self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
#                 k >>= 1

#         def query(self, l, r):
#             """
#             [l, r)のsegfuncしたものを得る
#             l: index(0-index)
#             r: index(0-index)
#             """
#             res = [self.ide_ele, self.ide_ele]

#             l += self.num
#             r += self.num
#             while l < r:
#                 if l & 1:
#                     res = self.segfunc(res, self.tree[l])
#                     l += 1
#                 if r & 1:
#                     res = self.segfunc(res, self.tree[r - 1])
#                 l >>= 1
#                 r >>= 1
#             return res


#     B = []
#     ans = []
#     for i in range(N):
#         B.append([A[i], i])
#     seg = SegTree(B, segfunc, ide_ele)
#     for i in range(Q):
#         #pdb.set_trace()
#         com, l, r = query[i][0], query[i][1], query[i][2]
#         if com == 1:
#             x = seg.tree[seg.num + l-1]
#             y = seg.tree[seg.num + r-1]
#             seg.update(l-1, [y[0], x[1]])
#             seg.update(r-1, [x[0], y[1]])
#         else:
#             ans.append(seg.query(l-1, r)[1]+1)
#     return ans
    
# if __name__ == '__main__':
#     N = 5
#     Q = 3
#     import random
#     A = [2, 1, 4, 3, 5]
#     # query = []
#     query = [[1, 1, 2], [2, 1, 3], [1, 2, 3]]
#     # for i in range(Q):
#     #     l, r = random.randint(1, N), random.randint(1, N)
#     #     if l > r:
#     #         l, r = r, l
#     #     query.append([i % 2 + 1, l, r])
#     m = main(N, Q, A, query)
#     aa = ac(N, Q, A, query)
#     if m != aa:
#         print(N, Q, A, query)
#         print(m, aa)

if __name__ == '__main__':
    main()