
class LazySegTree:
    def __init__(self, monoid: int, bottomList: "list[int]", func: "function", convertLengthToThePowerOf2: bool = False):
        print("index0 は使用されない。常にdefault値")
        self.monoid = monoid
        self.lazy_monoid = monoid
        self.func = func
        self.lazy_operation = func #遅延配列の要素同士の演算と、遅延配列から値配列への反映時の演算。
        if convertLengthToThePowerOf2:
            self.actualLen = len(bottomList)
            self.bottomLen = self.getSegLenOfThePowerOf2(len(bottomList))
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [monoid] * self.segLen
            self.lazy = [self.lazy_monoid] * self.segLen
        else:
            self.actualLen = len(bottomList)
            self.bottomLen = len(bottomList)
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [monoid] * self.segLen
            self.lazy = [self.lazy_monoid] * self.segLen
        self._build(bottomList)

    """
    初期化
    O(self.segLen)
    """
    def _build(self, seq):
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])

    """
    直近の2べきの長さを算出
    """
    def getSegLenOfThePowerOf2(self, ln: int):
        if ln <= 0:
            return 1
        else:    
            import math
            decimalPart, integerPart = math.modf(math.log2(ln))
            return 2 ** (int(integerPart) + 1)

    """
    一点加算 他演算
    O(log(self.bottomLen))
    """
    def pointAdd(self, i: int, val: int):
        i += self.offset
        self.tree[i] += val
        # self.tree[i] = self.func(self.tree[i], val) <- こっちの方が都度の修正は発生しない。再帰が遅くないか次第。
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

    """
    一点更新
    O(log(self.bottomLen))
    """
    def pointUpdate(self, i: int, val: int):
        i += self.offset
        self.tree[i] = val
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

    """
    遅延評価
    """
    def _lazyEval(self, idx: int):
        if self.lazy[idx] == 0:
            return
        # lazy[idx]の要素に遅延配列から反映
        self.tree[idx] = self.lazy_operation(self.tree[idx], self.lazy[idx])

        # 下の階層に伝播
        if r - l > 1:
            self.lazy[idx << 1] += self.lazy_operation(self.lazy[idx << 1], self.lazy[idx])
            self.lazy[idx << 1 | 1] += self.lazy_operation(self.lazy[idx << 1 | 1], self.lazy[idx])

        # lazy[idx]をクリア
        self.lazy[idx] = self.lazy_monoid

    def _propagate_to_bottom(self, top_idx: int):
        """
        最上部top_idxから底に向かって伝播していく。
        """
        height = top_idx.bit_length()
        for i in range(height, 0, -1): # 底は次に生きようがないので含まない。
            self._lazyEval(top_idx >> i) # 上から順に遅延評価する


    def getRange(self, l: int, r: int):
        """
        区間取得 (l ≦ X < r)
        l ~ r-1までの区間 (0-indexed)。※右端を含まない。
        O(log(self.bottomLen))
        """
        # 影響範囲において、遅延配列から値配列に反映
        l += self.offset
        r += self.offset
        vL = self.monoid
        vR = self.monoid
        top_l = l // (l & -l) # 奇数になるまでlを2で割ったもの。
        top_r = r // (r & -r) # 奇数になるまでlを2で割ったもの。
        self._propagate_to_bottom(top_l)
        self._propagate_to_bottom(top_r)

        # 区間の計算
        while l < r:
            print(l, r)
            if l & 1:
                vL = self.func(vL, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                vR = self.func(self.tree[r], vR)
            l >>= 1
            r >>= 1
        return self.func(vL, vR)

    """
    一点取得
    O(1)
    """
    def getPoint(self, i: int):
        i += self.offset
        return self.tree[i]

    """
    区間更新
    変更は遅延配列にマージするのみ。
    O(log(self.bottomLen))
    """
    def rangeUpdate(self, l: int, r: int, val: int):
        l += self.offset
        r += self.offset
        while l < r:
            if l & 1:
                self.lazy[l] = self.lazy_operation(self.lazy[l], val)
                l += 1
            if r & 1:
                r -= 1
                self.lazy[l] = self.lazy_operation(self.lazy[r], val)
            l >>= 1
            r >>= 1

print("#---case1---#")
# Usage
N = 8
# |               0               |
# |       0       |       0       |
# |   0   |   0   |   0   |   0   |
# | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | <- 0~7に対応

# モノイド
monoid = 0

# 利用する関数を定義
def add(A: int, B: int):
    return A + B

# 配列の初期化とビルド
seg = LazySegTree(monoid, [0, 1, 4, 9, 2, 5, 3, 1], add)
print(seg.tree) # [0, 25, 14, 11, 1, 13, 7, 4, 0, 1, 4, 9, 2, 5, 3, 1]

# |              25               | = seg.tree[1] ※ index0は使用しない。
# |      14       |      11       |
# |   1   |  13   |   7   |   4   |
# | 0 | 1 | 4 | 9 | 2 | 5 | 3 | 1 | <- 0~7に対応

seg.pointAdd(3 - 1, 10) # 3番目に10を加える。
print(seg.tree) # [0, 35, 24, 11, 1, 23, 7, 4, 0, 1, 14, 9, 2, 5, 3, 1]

seg.pointUpdate(7 - 1, 1) # 7番目を1に変更する。
print(seg.tree) # [0, 33, 24, 9, 1, 23, 7, 2, 0, 1, 14, 9, 2, 5, 1, 1]

num = seg.getRange(1, 6 + 1) # 1〜6番目までの要素の演算結果(func)を取得。右端を含まない。
print(num) # [0, <<<1, 14, 9, 2, 5, 1>>>, 1] -> 1 + 14 + 9 + 2 + 5 + 1 = 32

# |              33               |
# |      24       |       9       |
# |   1   |  23   |   7   |   2   |
# | 0 | 1 | 14| 9 | 2 | 5 | 1 | 1 |

seg.rangeUpdate(3, 8, 2)
print(seg.tree) # [0, 33, 24, 9, 1, 23, 7, 2, 0, 1, 14, 9, 2, 5, 1, 1] # まだ変わらない
print(seg.lazy) # [0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]

# |                      33/0                      |
# |         24/0           |          9/2          |
# |    1/0    |     23/0   |    7/0    |    2/0    |
# | 0/0 | 1/0 | 14/0 | 9/2 | 2/0 | 5/0 | 1/0 | 1/0 |


ans = seg.getRange(6, 7)
print(seg.tree) # [0, 33, 24, 11, 1, 23, 7, 4, 0, 1, 14, 9, 2, 5, 1, 1]
print(seg.lazy) # [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0, 0, 2, 2]

# |                      33/0                      |
# |         24/0           |         11/0          |
# |    1/0    |     23/0   |    7/2    |    4/0    |
# | 0/0 | 1/0 | 14/0 | 9/2 | 2/0 | 5/0 | 1/2 | 1/2 |
