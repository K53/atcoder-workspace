# ------------------------------------------------------------------------------
#     セグメント木 (1-indexed | 非2冪)
# ------------------------------------------------------------------------------
# 解説
# 1-indexed。頂点を除き末尾のビットが1なら右、0なら左。
#
# 以下は長さN=8のセグ木を宣言した場合。
# リストtreeが値を管理している。 tree全体の配列長を"segLen"
#   - index0は使用されない。
#   - index1-7は区間演算の結果の保持。
#   - index8-15は実際の値の保持。
# |                        [1]                          |
# |          [2]            |            [3]            |
# |    [4]    |     [5]     |     [6]     |     [7]     |
# | [8] | [9] | [10] | [11] | [12] | [13] | [14] | [15] | <- この実測値の部分の長さを"bottomLen"
#    ↑
#  実測値の開始インデックスを"offset"
#
# |                 [1]                 |
# |          [2]            |    [3]    |
# |    [4]    |     [5]     | [6] | [7] | <- 2冪でなくても後述の仕組みが成立するのでOK
# | [8] | [9] | [10] | [11] |         
#
# ================================================================================================================
# ■ _build()
# - index[7],[6],...[1]の順(=底部から順に)全部を演算し、初期化する。
#
# ================================================================================================================
# ■ pointAdd(i: int, val: int) / pointUpdate(i: int, val: int)
# - [i] → [i + offset]で内部のインデックスに変換後、影響範囲を全て更新。
# - [i + offset]を2で割り切ると必ず上の区間のインデックスに対応するので1になるまで2で割って最演算を繰り返す。
#
# ================================================================================================================
# ■ getRange(i: int)
# まず左を考える。
# |         [i]         |       [i + 1]       |  <- 1つ上の階層
# |   [2i]   | [2i + 1] |          |          |  <- 今見ている階層
# 左端が[2i]からの区間をとるなら、どうせ[2i + 1]も含むので上の階層の[i]を選択するほうが得。
# 逆に左端が[2i + 1]からの区間を取るなら、[2i + 1]は取らざるを得ない。
# → 左側の部屋[2i]にいるならそのまま真上の階の部屋[i]へ行く。
# → 右側の部屋[2i + 1]にいるならそのその値は読み取ってから次の階の右隣の部屋[i + 1]に行く。 (左右どちらの部屋にいるかはインデックスが偶数なら左、奇数なら右とわかる。)
#
# 右も同様に考える(ただし、rは含まないので注意)ことで、奇数(右の部屋)なら左に進んでからその値を取って、真上の階へ(繰り返すが、rは含まないのでこれでいい)
# 偶数ならそのまま真上に進む。
# ※ ここでrはどうやっても真上の部屋にしか進まないことがわかる!!!
# → lは真上か右上の部屋兵器売るがrは真上なのでクロスしてしまうことがあり得ないと言える。
# → よって、この操作を行うのは l < r が成り立つ間だけ。もっと言えば(l == r)になったら終了。
#
# ================================================================================================================
#
# Note
# - 2冪でなくてもいい。
#
# リンク
# https://maspypy.com/segment-tree-%e3%81%ae%e3%81%8a%e5%8b%89%e5%bc%b71
#
# 計算量
# 
# 依存関係
# EulerTour.py から依存されている
#
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A&lang=ja # Range Min Query (RMQ)
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja # Range Sum Query (RSQ)
# - https://atcoder.jp/contests/arc033/submissions/31404125 # セグ木の二分探索 / セグ木上の二分探索
# - https://yukicoder.me/submissions/757494 # セグ木の二分探索 (yuki 833)
# - https://yukicoder.me/submissions/757820 # セグ木上の二分探索 (yuki 833) 上より100~200ms高速
# - https://yukicoder.me/submissions/757554 # インデックス付きのセグ木
# - https://yukicoder.me/submissions/632551 # セグ木上の二分探索
# - https://yukicoder.me/submissions/817123 # 複数要素のセグ木
# - https://atcoder.jp/contests/abc185/tasks/abc185_f # XORのセグ木
# ------------------------------------------------------------------------------

class SegTree:
    def __init__(self, monoid: int, bottomList: "list[int]", func: "function", convertLengthToThePowerOf2: bool = False):
        print("index0 は使用されない。常にdefault値")
        self.monoid = monoid
        self.func = func
        if convertLengthToThePowerOf2:
            self.actualLen = len(bottomList)
            self.bottomLen = self.getSegLenOfThePowerOf2(len(bottomList))
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [monoid] * self.segLen
        else:
            self.actualLen = len(bottomList)
            self.bottomLen = len(bottomList)
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [monoid] * self.segLen
        self._build(bottomList)

    def _build(self, seq):
        """
        初期化
        O(self.segLen)
        """
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])

    def getSegLenOfThePowerOf2(self, ln: int):
        """
        直近の2べきの長さを算出
        """
        if ln <= 0:
            return 1
        else:    
            import math
            decimalPart, integerPart = math.modf(math.log2(ln))
            return 2 ** (int(integerPart) + 1)

    def pointAdd(self, i: int, val: int):
        """
        一点加算 他演算
        O(log(self.bottomLen))
        """
        i += self.offset
        self.tree[i] += val
        # self.tree[i] = self.func(self.tree[i], val) <- こっちの方が都度の修正は発生しない。再帰が遅くないか次第。
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

    def pointUpdate(self, i: int, val: int):
        """
        一点更新
        O(log(self.bottomLen))
        """
        i += self.offset
        self.tree[i] = val
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

    def getRange(self, l: int, r: int):
        """
        区間取得 (l ≦ X < r)
        l ~ r-1までの区間 (0-indexed)。※右端を含まない。
        O(log(self.bottomLen))
        """
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

    def getPoint(self, i: int):
        """
        一点取得
        O(1)
        """
        i += self.offset
        return self.tree[i]

    def max_right(self, l, is_ok: "function"):
        """
        二分探索
        O(log(self.bottomLen))
        ※ セグ木上の二分探索をする場合は2べきにすること。
        # !!!! ng側が返却される !!!!!
        """
        print("セグ木上の二分探索をする場合は2べきにすること。")
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
        return ll - self.offset # ng側が返る

    # 未検証
    def min_left(self, r, is_ok):
        r += self.offset
        rr = max(r // (~r & -~r), 1)
        ans = self.monoid
        while is_ok(self.func(self.tree[rr], ans)):
            ans = self.func(self.tree[rr], ans)
            rr -= 1
            while rr & 1:
                rr >>= 1
            if rr == 0:
                return -1
        while rr < self.offset:
            rr <<= 1
            if is_ok(self.func(self.tree[rr+1], ans)):
                ans = self.func(self.tree[rr+1], ans)
            else:
                rr += 1
        return rr - self.offset

if __name__ == "__main__":
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
    print(seg.tree) # [0, 35, 24, 11, 1, 23, 7, 4, 0, 1, 14, 9, 2, 5, 3, 1]

    # |              35               |
    # |      24       |      11       |
    # |   1   |  23   |   7   |   4   |
    # | 0 | 1 | 14| 9 | 2 | 5 | 3 | 1 |

    seg.pointUpdate(7 - 1, 1) # 7番目を1に変更する。
    print(seg.tree) # [0, 33, 24, 9, 1, 23, 7, 2, 0, 1, 14, 9, 2, 5, 1, 1]

    num = seg.getRange(1, 6 + 1) # 1〜6番目までの要素の演算結果(func)を取得。右端を含まない。
    print(num) # [0, <<<1, 14, 9, 2, 5, 1>>>, 1] -> 1 + 14 + 9 + 2 + 5 + 1 = 32


    # =====================================================
    #     case2
    # =====================================================
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
    exit()

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

    # ng側が返るので注意。 K番目の要素算出では x < K とすることでng側が答えになる。
    print(seg.max_right(0, lambda x: x < 1)) # 1番目の要素 → 1
    print(seg.max_right(0, lambda x: x < 2)) # 2番目の要素 → 3
    print(seg.max_right(0, lambda x: x < 3)) # 3番目の要素 → 4
    print(seg.max_right(0, lambda x: x < 4)) # 4番目の要素 → 4


    print(seg.min_left(-1, lambda x: x < 1)) # 4
    print(seg.min_left(-1, lambda x: x < 2)) # 4
    print(seg.min_left(-1, lambda x: x < 3)) # 3
    print(seg.min_left(-1, lambda x: x < 4)) # 1

