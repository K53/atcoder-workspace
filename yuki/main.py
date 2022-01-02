#!/usr/bin/env python3
from sys import stdin
class SegmentTree:
    def __init__(self, monoid: int, bottomLen: int):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen

    """ 一点加算 区間和 (RSQ)
    """
    def pointAdd(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.tree[segIndex * 2] + self.tree[segIndex * 2 + 1]
        return

    """ 区間和 (RSQ)
    """
    def rangeSumQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = 0
        while l < r:
            if l % 2 == 1:
                res += self.tree[l]
                l += 1
            l //= 2
            if r % 2 == 1:
                res += self.tree[r - 1]
                r -= 1
            r //= 2
        return res

def main():
    tr = SegmentTree(monoid=0, bottomLen=2**18)
    
    return
            

if __name__ == '__main__':
    main()