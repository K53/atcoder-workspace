# ------------------------------------------------------------------------------
#     セグメント木 (1-indexed)
# ------------------------------------------------------------------------------
# 解説
# 1-indexed。頂点を除き末尾のビットが1なら左、0なら右。
#
# リンク
# https://maspypy.com/segment-tree-%e3%81%ae%e3%81%8a%e5%8b%89%e5%bc%b71
# 計算量
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A&lang=ja # Range Min Query (RMQ)
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja # Range Sum Query (RSQ)
# - https://atcoder.jp/contests/arc033/tasks/arc033_3 # セグ木の二分探索 / セグ木上の二分探索
# - https://yukicoder.me/submissions/757494 # セグ木の二分探索
# - https://yukicoder.me/submissions/757554 # インデックス付きのセグ木
# - https://yukicoder.me/submissions/632551 # セグ木上の二分探索
# ------------------------------------------------------------------------------

# 2冪に変換するための長さ算出処理
def getSegLenOfThePowerOf2(ln: int):
    if ln <= 0:
        return 1
    else:    
        import math
        decimalPart, integerPart = math.modf(math.log2(ln))
        return 2 ** (int(integerPart) + 1)

# 2べきでなくてもいい
class SegTree:
    def __init__(self, monoid, bottomList, func):
        self.monoid = monoid
        self.func = func
        self.bottomLen = len(bottomList)
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [monoid] * self.segLen
        self.build(bottomList)

    """
    初期化
    O(self.segLen)
    """
    def build(self, seq):
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])

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
    
    # """ # 未検証 多分動かない -> LazySegmentTreeへ
    # 区間更新
    # O(log(self.bottomLen))
    # """
    # def rangeUpdate(self, l: int, r: int, val: int):
    #     l += self.offset
    #     r += self.offset
    #     while l < r:
    #         if l & 1:
    #             self.tree[l] = self.func(self.tree[l], val) 
    #             l += 1
    #         if r & 1:
    #             r -= 1
    #             self.tree[r] = self.func(self.tree[r], val) 
    #         l >>= 1
    #         r >>= 1
    #     return

    """
    区間取得
    O(log(self.bottomLen))
    """
    def getRange(self, l: int, r: int):
        l += self.offset
        r += self.offset
        vL = self.monoid
        vR = self.monoid
        while l < r:
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
    O(log(self.bottomLen))
    """
    def getPoint(self, i: int):
        i += self.offset
        return self.tree[i]

    """
    二分探索
    O(log(self.bottomLen))
    ※ セグ木上の二分探索を使う場合は2べきにすること。
    """
    def queryKthItem(self, K: int):
        print("セグ木上の二分探索を使う場合は2べきにすること。")
        index = 1
        restK = K
        while index < self.offset:
            if restK <= self.tree[index << 1]:
                index <<= 1
            else:
                restK -= self.tree[index << 1] # 左に進む場合は右側の分を差し引く。
                index <<= 1
                index += 1
        return index - self.offset

    def max_right(self, l, is_ok: "function"):
        l += self.offset
        ll = l // (l & -l) # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
        ans = self.monoid
        while is_ok(self.func(ans, self.tree[ll])): # そのセグメントが条件を満たすかどうかの判定
            ans = self.func(ans, self.tree[ll])
            ll += 1
            while ~ll & 1: # llの反転 ~ll = -(ll+1)
                ll >>= 1 # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
            if ll == 1: # 最上層まで到達したら全範囲満たすということ。 → (2べきになるようにモノイド埋めする前の)実際の長さを返す。
                return self.actualLen
        while ll < self.offset:
            ll <<= 1 # 一階層下のセグメントへ移動 (=2倍)
            if is_ok(self.func(ans, self.tree[ll])): # 条件を満たすなら同一階層の隣のセグメントの下層へ。満たさないならそのまま下層へ。
                ans = self.func(ans, self.tree[ll])
                ll += 1
        return ll - self.offset # ng側が返る？？

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
seg = SegTree(monoid, [0, 1, 4, 9, 2, 5, 3, 1], add)
print(seg.tree) # [0, 25, 14, 11, 1, 13, 7, 4, 0, 1, 4, 9, 2, 5, 3, 1]

# |              25               | = seg.tree[1] ※ index0は使用しない。
# |      14       |      11       |
# |   1   |  13   |   7   |   4   |
# | 0 | 1 | 4 | 9 | 2 | 5 | 3 | 1 | <- 0~7に対応

seg.pointAdd(3 - 1, 10) # 3番目に10を加える。
seg.pointUpdate(7 - 1, 1) # 7番目を1に変更する。

seg.getRange(1, 6 + 1) # 1〜6番目までの要素の演算結果(func)を取得。右端を含まない。

# === case2
print("#---case2---#")
N = 6

# モノイド
monoid = 0

# 利用する関数を定義
def add(A: int, B: int):
    return A + B

# 配列の初期化とビルド
seg = SegTree(monoid, [0, 1, 4, 9, 2, 5], add)

print(seg.tree) # [0, 21, 20, 1, 13, 7, 0, 1, 4, 9, 2, 5]

# |           21          | = seg.tree[1] ※ index0は使用しない。
# |      20       |   1   |
# |  13   |   7   | 0 | 1 |  <- 0 ~ 5
# | 4 | 9 | 2 | 5 |          <- に対応

print(seg.getRange(0, 2 + 1)) # 5 = 0 + 1 + 4

# セグ木の二分探索 (セグ木外)

# eg) 左端からの累積和が5以下を満たす最大の要素を取り出したい。
# True ------ ok | ng ---- False
def is_ok(k: int, threshold: int):
    return seg.getRange(0, k + 1) <= threshold   # 条件式

def binSearch(ok: int, ng: int, threshold: int):
    # print(ok, ng)              # はじめの2値の状態
    while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
        mid = (ok + ng) // 2
        # print("target > ", mid)
        result = is_ok(mid, threshold)
        # print(result)
        if result:
            ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
        else:
            ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
        # print(ok, ng)          # 半分に切り分ける毎の2値の状態
    return ok    # 関数呼び出し時の引数のngは絶対評価されないのでngに書く値が答えになりうるならその数マイナス1を指定する。

threshold = 5
ans = binSearch(0, N + 1, threshold)
print(ans) # 2 ->  [0, 1, "4", 9, 2, 5]

# セグ木上の二分探索
print("#---case3---#")

# モノイド
monoid = 0

N = 5

# 利用する関数を定義
def add(A: int, B: int):
    return A + B

# 配列の初期化とビルド
seg = SegTree(monoid, [0, 1, 0, 1, 2, 0, 0, 0], add) # 2べきになるように末尾にモノイドを追加

print(seg.tree) # [0, 4, 2, 2, 1, 1, 2, 0, 0, 1, 0, 1, 2, 0, 0, 0]

# |               4               | = seg.tree[1] ※ index0は使用しない。
# |       2       |       2       |
# |   1   |   1   |   2   |   0   |
# | 0 | 1 | 0 | 1 | 2 | 0 | 0 | 0 | <- 0~7に対応

print(seg.queryKthItem(1)) # 1
print(seg.queryKthItem(2)) # 3
print(seg.queryKthItem(3)) # 4
print(seg.queryKthItem(4)) # 4
print(seg.queryKthItem(5)) # 7
