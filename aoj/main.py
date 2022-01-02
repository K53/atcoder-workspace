#!/usr/bin/env python3

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
    N = int(input())
    a = list(map(int, input().split()))
    tr = SegmentTree(monoid=0, bottomLen=2**18)
    ans = 0
    for i in range(N):
        aa = a[i]
        tr.pointAdd(aa, 1)
        num = tr.rangeSumQuery(0, aa + 1)
        # print(i - (num - 1))
        ans += i - (num - 1)
    print(ans)

if __name__ == '__main__':
    main()