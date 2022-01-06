# ------------------------------------------------------------------------------
#     インデックス付きセグメント木 (1-indexed) Range Min Query (RMQ)
# ------------------------------------------------------------------------------
# 解説
# index 0は使用しない。ノードNの子はノード2Nとノード2N+1
#
# リンク
# 
# 計算量
# 
# verify
# - https://yukicoder.me/problems/no/875
# - (提出) https://yukicoder.me/submissions/728334
# ------------------------------------------------------------------------------
#!/usr/bin/env python3
class SegmentTree:
    def __init__(self, monoid: int, bottomLen: int, operation: "function"):
        self.monoid = monoid
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.bottomLen + [[i, monoid] for i in range(self.bottomLen)]  # 最下層以外はインデックスのない配列を初期値にしているが、のちにallBuild()するのであれば問題ない。
        self.operation = operation
        return
    
    """ 1点取得
    O(1)
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

    """ 1点更新 + リビルド
    O(log(bottomLen))
    """
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

def main():
    INF = 10 ** 6
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    tr = SegmentTree(monoid=INF, bottomLen=2**18, operation=minWithIndex)
    for i in range(N):
        tr.pointUpdateWithoutRebuild(i, A[i])
    tr.allBuild()
    for i in range(Q):
        t, l, r = map(int, input().split())
        if t == 1: # l - 1 と r - 1 のSWAP
            al, ar = tr.getPoint(l - 1), tr.getPoint(r - 1)
            tr.pointUpdate(l - 1, ar[1])
            tr.pointUpdate(r - 1, al[1])
            # print(tr.tree)
        else: # l - 1 〜 r - 1 の区間の最小値を与えるインデックスを出力。
            i, _ = tr.rangeQuery(l - 1, r)
            print(i + 1)
            # print(tr.tree)
    return            

if __name__ == '__main__':
    main()