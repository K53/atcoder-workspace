#!/usr/bin/env python3
import sys
input = lambda: sys.stdin.readline().strip()

def main():
    N, Q = map(int, input().split())
    c = list(map(int, input().split()))
    
    wait_col = [-1] * (N + 1)
    latest = [-1] * N
    for i in range(N):
        latest[i] = wait_col[c[i]]
        wait_col[c[i]] = i
    # print(latest)

    ox_col = [0] * (N + 1)
    ox = [0] * N
    for i in reversed(range(N)):
        if ox_col[c[i]] == 1:
            continue
        ox_col[c[i]] = 1
        ox[i] = 1
    # print(ox)
    class SegTree:
        def __init__(self):
            self.offset = N        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = N * 2
            self.tree = [0] * N + ox
            # ビルド
            for i in range(self.offset - 1, 0, -1):
                self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

        """
        一点加算 他演算
        O(log(self.bottomLen))
        """
        def pointAdd(self, i: int, val: int):
            i += self.offset
            self.tree[i] += val
            while i > 1:
                i >>= 1 # 2で割って頂点に達するまで下層から遡上
                self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1] # 必ず末尾0と1がペアになるのでor演算子

        """
        区間取得
        l ~ r-1までの区間 (0-indexed)。※右端を含まない。
        O(log(self.bottomLen))
        """
        def getRange(self, l: int, r: int):
            l += self.offset
            r += self.offset
            vL = 0
            vR = 0
            while l < r:
                if l & 1:
                    vL +=self.tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    vR += self.tree[r]
                l >>= 1
                r >>= 1
            return vL + vR

    seg = SegTree()

    queries = []
    for i in range(Q):
        l, r = map(int, input().split())
        queries.append((r - 1 + 1, l - 1, i))
    queries.sort(reverse=True)
    prev_r = N
    ans = [0] * Q
    for r, l, i in queries:
        # print(r, l, i)
        for ri in range(r, prev_r):
            if ri <= latest[ri]:
                continue
            seg.pointAdd(ri, -1)
            seg.pointAdd(latest[ri], 1)
        prev_r = r
        # print(seg.tree[seg.bottomLen:], seg.getRange(l, r))
        ans[i] = seg.getRange(l, r)
    print(*ans, sep="\n")
    return

if __name__ == '__main__':
    main()
