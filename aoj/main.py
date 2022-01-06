#!/usr/bin/env python3

class SegmentTree:
    def __init__(self, monoid: int, bottomLen: int, operation: "function"):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen
        self.operation = operation
        return
    
    """ 1点更新
    O(1)
    """
    def pointUpdateWithoutRebuild(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val          # 各マスの更新方法
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
        self.tree[segIndex] += val          # 各マスの更新方法
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.operation(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
        return

    def rangeQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = self.monoid                   # クエリの初期値
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

def add(a: int, b: int):
    return a + b

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    queries = []
    qq = []
    for i in range(N):
        qq.append((A[i], i, 0))
    tr = SegmentTree(monoid=0, bottomLen=2**18, operation=add)
    count = SegmentTree(monoid=0, bottomLen=2**18, operation=add)
    for i in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)
        qq.append((query[-1], i, 1))
    qq.sort()
    ans = [-1] * Q
    # print(qq)
    for qqq in qq[::-1]:
        # print(qqq)
        if qqq[2] == 0:
            tr.pointUpdate(qqq[1], qqq[0])
            count.pointUpdate(qqq[1], 1)
        else:
            num = tr.rangeQuery(queries[qqq[1]][1] - 1, queries[qqq[1]][2])
            c = count.rangeQuery(queries[qqq[1]][1] - 1, queries[qqq[1]][2])
            ans[qqq[1]] = num - c * queries[qqq[1]][3]
        # print(tr.tree)
    print(*ans, sep="\n")
    return


if __name__ == '__main__':
    main()