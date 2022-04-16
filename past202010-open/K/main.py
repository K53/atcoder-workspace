#!/usr/bin/env python3
import sys
MOD = 10 ** 9  # type: int

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
    K = int(input())
    inv = []
    Ns = []
    As = []
    count = []
    for _ in range(K):
        n = int(input())
        Ns.append(n)
        a = list(map(int, input().split()))
        As.append(a)
        tr = SegmentTree(monoid=0, bottomLen=32)
        ans = 0
        tmpcount = [0] * 21
        for i in range(n):
            num = a[i]
            tmpcount[a[i]] += 1
            tr.pointAdd(num, 1)
            ans += i + 1 - tr.rangeSumQuery(0, num + 1)
            ans %= MOD
        count.append(tmpcount)
        inv.append(ans)
    

    Q = int(input())
    b = list(map(lambda i: int(i) - 1, input().split()))
    ans = 0
    totaltr = SegmentTree(monoid=0, bottomLen=32)
    for bb in b:
        ans += inv[bb]
        n = Ns[bb]
        a = As[bb]
        c = count[bb]
        for i in range(21):
            # print(i, c[i], "#")
            if c[i] != 0:
                num = totaltr.tree[1] - totaltr.rangeSumQuery(0, i + 1)
                ans += num * c[i]
        for i in range(21):
            if c[i] != 0:
                totaltr.pointAdd(i, c[i])

    print(ans % MOD)
    return

if __name__ == '__main__':
    main()
