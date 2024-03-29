#!/usr/bin/env python3
import sys
import math

class SegmentTree:
    def __init__(self, monoid: int, bottomLen: int):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen

    """ 一点更新 区間最小値 (RMQ)
    tree[index] = val
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = [max(self.tree[segIndex * 2][0], self.tree[segIndex * 2 + 1][0]), min(self.tree[segIndex * 2][-1], self.tree[segIndex * 2 + 1][-1])]
            # self.tree[segIndex] = min(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
        return

    """ 区間最小値 (RMQ)
    """
    # def rangeMinQuery(self, l: int, r: int):
    #     l += self.offset
    #     r += self.offset
    #     res = self.monoid
    #     while l < r:
    #         if l % 2 == 1:
    #             res = min(res, self.tree[l])
    #             l += 1
    #         l //= 2
    #         if r % 2 == 1:
    #             res = min(res, self.tree[r - 1])
    #             r -= 1
    #         r //= 2
    #     return res

    def initBottom(self, bottomList: list):
        self.tree[self.offset:] = bottomList
        preLayer = self.offset
        layer = self.offset // 2
        while layer >= 1:
            for segIndex in range(layer, preLayer):
                self.tree[segIndex] = [max(self.tree[segIndex * 2][0], self.tree[segIndex * 2 + 1][0]), min(self.tree[segIndex * 2][-1], self.tree[segIndex * 2 + 1][-1])]
            layer //= 2
        return
    
    def q(self, x, y):
        index = 1
        if self.tree[index] >= K:
            return 0
        while index < self.offset:
            if self.tree[2 * index] < K: # 左側にその寿司を食べたい奴がいる
                index = 2 * index
            else:
                index = 2 * index + 1
        return index - self.offset





# Range Minimum Query
# tr = SegmentTree(monoid=INF, bottomLen=2**18)
# tr.pointUpdate(1, 1)
# tr.pointUpdate(2, 2)
# tr.pointUpdate(3, 3)
# print(tr.rangeMinQuery(1, 2 + 1)) # セグ木は右側は開区間として計算しているので+1必要。


def solve(N: int, X: int, Y: int, A: "List[int]"):
    INF = 10 ** 9
    p, q = math.modf(math.log2(N))
    print(p, q)
    seglen = int(q) + 1
    # seglen = 2
    # print(N)
    # print(2**seglen)
    tr = SegmentTree(monoid=[-INF, INF], bottomLen=2**seglen)
    tr.initBottom([[aa, aa] for aa in A] + [[-INF, INF] for _ in range(2**seglen - N)])
    print(tr.tree)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, Y, A)

if __name__ == '__main__':
    main()
