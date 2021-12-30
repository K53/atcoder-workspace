#!/usr/bin/env python3
import sys

class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int, func: "function(int, int)"):
        self.initVal = initVal
        self.func = func
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    """ 一点更新
    tree[index] = val
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = self.func(self.tree[segIndex], val) # Update
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])

    """ 区間最小値 (RMQ)
    """
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

def myXor(a, b):
    return a ^ b

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    tr = SegmentTree(initVal=0, bottomLen=(N), func=myXor)
    for nn in range(N):
        tr.pointUpdate(index=nn, val=A[nn])
    for _ in range(Q):
        T, X, Y = map(int, input().split())
        if T == 1:
            tr.pointUpdate(X - 1, Y)
        else:
            print(tr.rangeQuery(X - 1, Y))


    
    
if __name__ == '__main__':
    main()