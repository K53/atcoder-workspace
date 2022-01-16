#!/usr/bin/env python3
import sys


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

    """ 二分探索
    O(log(bottomLen))
    """
    def queryKthItem(self, K: int):
        index = 1   # セグ木の頂点が開始
        restK = K
        while index < self.offset:  # 最下層に到達するまで回す
            if restK <= self.tree[2 * index]:   # 右に行く条件
                index = 2 * index
            else:                               # 左に行く条件
                restK -= self.tree[2 * index]   # 左に進む場合は右側の分を差し引く。
                index = 2 * index + 1
        return index - self.offset

def add(a: int, b: int):
    return a + b

def solve(N: int, K: int, P: "List[int]"):
    tr = SegmentTree(monoid=0, bottomLen=2**19, operation=add)
    for pp in P[:K]:
        tr.pointUpdateWithoutRebuild(pp, 1)
    tr.allBuild()
    print(tr.queryKthItem(1))
    for i in range(N - K):
        tr.pointUpdate(P[K + i], 1)
        print(tr.queryKthItem(i + 2))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    P = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, P)

if __name__ == '__main__':
    main()