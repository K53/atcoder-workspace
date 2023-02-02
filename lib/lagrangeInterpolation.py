# ------------------------------------------------------------------------------
#     (MOD下における) ラグランジュ補間  (Lagrange Interpolation)
# ------------------------------------------------------------------------------
# 解説
# - ラグランジュ補間 とは？
# - x座標の相異なる(N+1)点[(x_0, y_0), (x_1, y_1),・・・(x_N, y_N)]を通るN次以下の関数y = P(x)は一意に定まる。
# - P(x)の算出方法は数学的な式は参考リンク参照。
# なお、点を通ることは言い換えると y=P(x) を満たす(x, y)と言える。すなわち、
#       多項式P(x) が P(x_i)=y_i (i=0,…,N) を満たす。
# 
# 式変形とアルゴリズム
#
#                         Π(x - x[k])
#           n            (k≠i)            
#    P(x) = Σ y[i] * -------------------
#            i=0         Π(x[i] - x[k])     
#                        (k≠i)
#           n                                              
#         = Σ Q[i] * Π(x - x[k])
#          i=0      (k≠i)         
#
#
#           n         (x - x[0])(x - x[1])・・・(x - x[k])
#         = Σ Q[i] * -------------------------------------
#          i=0                     (x - x[i])
#
#           n             R
#         = Σ Q[i] * ------------
#          i=0        (x - x[i])
#
# なお、QおよびRは以下、
#
#               y[i]
# Q[i] = ------------------ : ラグランジュ補間公式におけるi項目のQ[i]。i番目の点(points[i])に関する項 (iは0-indexed)
#          Π(x[i] - x[k])
#         (k≠i)
# 
# R = Π(x - x[k])
#
# Note
# - 与えられる点にx座標の重複がないこと。 [(-1, 0), (0, 0), (1, 1), (1, 10)] とかはNG。x=1が重複
# - (N+1)点を与えるとN次以下の関数が帰る。P(x)=0も含む。
#
# 参考
# - https://manabitimes.jp/math/726
#
# verify
# - https://atcoder.jp/contests/abc137/tasks/abc137_f
# ------------------------------------------------------------------------------
from functools import lru_cache
def lagrangeInterpolation(points: "list[tuple(int, int)]", MOD: int) -> "list[int]":

    @lru_cache(maxsize=None)
    def modinv(a: int):
        b = MOD
        u, v = 1, 0
        while b:
            p, q = divmod(a, b)
            a, b = b, q
            u, v = v, u - p * v
        return u % MOD

    N = len(points)
    #
    #               y[i]
    # Q[i] = ------------------ : ラグランジュ補間公式におけるi項目のQ[i]。i番目の点(points[i])に関する項 (iは0-indexed)
    #          Π(x[i] - x[k])
    #         (k≠i)
    #
    Q = []
    for i in range(N):
        x_i, y_i = points[i]
        denominator = 1
        for k in range(N):
            x_k, y_k = points[k]
            if i == k:
                continue
            denominator *= x_i - x_k
            denominator %= MOD
        Q.append(modinv(denominator) * y_i % MOD)

    # DP的に求める。
    # R[i] = Π(x - x[i]) := i項目まで掛けた(たすき掛けした)時のx^jの係数はR[i][j] (mod MOD) 
    # ※ 便宜上i=0はどの項も選択されていない状態でR[0]=定数1とする。
    #
    # R[i + 1] = R[i] * (x - x[i + 1]) の漸化式なのでDP的に解く。
    #
    # なお、全てのiについて結果を保持しておく必要がないのでここではRを二次元配列にせずR = calcedRとして上書きし、末尾にあたるR[-1]のみを持つようにしている。
    #
    R = [1] + [0] * N # 定数c = 1のみの項。
    for i in range(N): # i項目の (x - x[i])を掛けた後の係数を算出する。
        x_i, y_i = points[i]
        calcedR = [0] * (N + 1)
        # x^jの係数にたすき掛け。
        # (・・多項式・・) * (x - x[i + 1]) の定数側の係数(-x[i + 1])を掛ける処理
        for j in range(N):
            calcedR[j] += -x_i * R[j]
            calcedR[j] %= MOD
        # (・・多項式・・) * (x - x[i + 1]) のx側の係数(1)を掛ける処理
        for j in range(N):
            calcedR[j + 1] += 1 * R[j]
            calcedR[j + 1] %= MOD
        R = calcedR

    # P(x)の各項の係数を算出する。
    #        n             R
    # P(x) = Σ Q[i] * ------------
    #       i=0        (x - x[i])
    #
    coef = [0] * N
    for i in range(N):
        x_i, y_i = points[i]
        if Q[i] == 0:
            continue
        # (x - x[i])の項 すなわち (x - x[i]) で割る。
        # Rの最大の次数の項を(x - x[i])のxの係数1で割る。次の項の次数からその分引き算してから次の項を1で割る。
        # これを繰り返す。先頭から割り算していく多項式同士の割り算の筆算のイメージ. 
        # なお、ここでは使わないので上書きしているがprev_carriedを繋ぎ合わせたらR / (x - x[i])の商になる。
        prev_carried = 0
        for j in range(N):
            j = N - j # reversed(range(N))で回してもいいがやや遅い印象
            next_carry = ((R[j] - prev_carried * -x_i) % MOD) * modinv(1) % MOD
            coef[j - 1] += next_carry * Q[i] % MOD
            coef[j - 1] %= MOD
            prev_carried = next_carry
    return coef


# ------------------------------------------------------------------------------
###  OLD v2
# ------------------------------------------------------------------------------
# 分岐が多くて可読性が低い。
# verify
# - https://atcoder.jp/contests/abc137/submissions/38476903
# ------------------------------------------------------------------------------
# from functools import lru_cache
# def lagrangeInterpolation(points: "list[tuple(int, int)]", MOD: int) -> "list[int]":
#     # 多項式P(x) が P(xi)=yi (i=0,…,n) を満たす時
#     # 
#     #                   Π(x - x[k])
#     #        n         (k≠i)            
#     # P(x) = Σ y[i] * ----------------- 
#     #       i=0         Π(x[i] - x[k])     
#     #                  (k≠i)
#     #        n                                              
#     #      = Σ Q[i] * Π(x - x[k])
#     #       i=0      (k≠i)         
#     #
#     #
#     #        n         (x - x[0])(x - x[1])・・・(x - x[k])
#     #      = Σ Q[i] * -------------------------------------
#     #       i=0                     (x - x[i])
#     #
#     #        n             R
#     #      = Σ Q[i] * ------------
#     #       i=0        (x - x[i])
#     #
#     N = len(points)

#     @lru_cache(maxsize=None)
#     def modinv(a: int):
#         b = MOD
#         u, v = 1, 0
#         while b:
#             p, q = divmod(a, b)
#             a, b = b, q
#             u, v = v, u - p * v
#         return u % MOD

#     #
#     #               y[i]
#     # Q[i] = ------------------ : ラグランジュ補間公式におけるi項目のQ[i]。i番目の点(points[i])に関する項 (iは0-indexed)
#     #          Π(x[i] - x[k])
#     #         (k≠i)
#     #
#     Q = []
#     for i in range(N):
#         x_i, y_i = points[i]
#         denominator = 1
#         for k in range(N):
#             x_k, y_k = points[k]
#             if i == k:
#                 continue
#             denominator *= x_i - x_k
#             denominator %= MOD
#         Q.append(modinv(denominator) * y_i % MOD)

#     #
#     # DP的に求める。
#     # R[i] = Π(x - x[i]) := i項目まで掛けた(たすき掛けした)時のx^jの係数はR[i][j] (mod MOD) 
#     # ※ 便宜上i=0はどの項も選択されていない状態でR[0]=定数1とする。
#     #
#     # R[i + 1] = R[i] * (x - x[i + 1]) の漸化式なのでDP的に解く。
#     #
#     # なお、全てのiについて結果を保持しておく必要がないのでここではRを二次元配列にせずR = calcedRとして上書きし、末尾にあたるR[-1]のみを持つようにしている。
#     #
#     R = [1] + [0] * N # 定数c = 1のみの項。
#     for i in range(N): # i項目の (x - x[i])を掛けた後の係数を算出する。
#         x_i, y_i = points[i]
#         calcedR = [0] * (N + 1)
#         # === x^jの係数にたすき掛け。==============
#         # (・・多項式・・) * (x - x[i + 1]) の定数側の係数(-x[i + 1])を掛ける処理
#         for j in range(N):
#             calcedR[j] += -x_i * R[j]
#             calcedR[j] %= MOD
#         # (・・多項式・・) * (x - x[i + 1]) のx側の係数(1)を掛ける処理
#         for j in range(N):
#             calcedR[j + 1] += 1 * R[j]
#             calcedR[j + 1] %= MOD
#         R = calcedR
#     # print(R) 

#     # P(x)の各項の係数を算出する。
#     #        n             R
#     # P(x) = Σ Q[i] * ------------
#     #       i=0        (x - x[i])
#     #
#     coef = [0] * N
#     for i in range(N):
#         x_i, y_i = points[i]
#         if Q[i] == 0:
#             continue
#         if x_i == 0: 
#             # (x - 0)の項 すなわち x で割るので全ての係数を1つ落としたものを加えたらいい。 R[j] → R[j + 1]を使用。
#             # この分岐処理をなくしてelse以下と同じ処理をしてもいいがそのままだとpow(0, -1)が死ぬので注意。
#             for j in range(N):
#                 coef[j] += R[j + 1] * Q[i] % MOD
#                 coef[j] %= MOD
#         else:
#             # (x - x_i)の項 すなわち (x - x_i) で割る。 (x_i ≠ 0)
#             # P(x)の最大次の項は 1 にのみ影響されるので 1 で割るのみ。
#             # print(R)
#             prev = R[N] * modinv(1) % MOD
#             coef[N - 1] += prev * Q[i] % MOD
#             coef[N - 1] %= MOD
#             # print("PRE", prev)
#             # print(coef)
#             # P(x)のx^jの係数の項は 頭から
#             # print(coef)
#             for j in range(N - 1):
#                 j = N - 1 - j 
#                 next = ((R[j] - prev * -x_i) % MOD) * modinv(1) % MOD
#                 coef[j - 1] += next * Q[i] % MOD
#                 coef[j - 1] %= MOD
#                 prev = next

# ------------------------------------------------------------------------------
###  OLD v1
# ------------------------------------------------------------------------------
# P(x)の各項の係数を算出にあたりR / (x -x[i])を定数項から昇順に算出していくもの。
# ラグランジュ補間では問題にならないが、一般によくある多項式同士の割り算に応用できない(あまりがある場合に対応できない)ため汎用性が低いと見て書き直した。
#
# verify
# - https://atcoder.jp/contests/abc137/submissions/38475087
# ------------------------------------------------------------------------------
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def modinv(a: int, mod: int):
#     b = mod
#     u, v = 1, 0
#     while b:
#         p, q = divmod(a, b)
#         a, b = b, q
#         u, v = v, u - p * v
#     return u % mod

# def lagrangeInterpolation(points: "list[tuple(int, int)]", MOD: int) -> "list[int]":
#     # 多項式P(x) が P(xi)=yi (i=0,…,n) を満たす時
#     # 
#     #                   Π(x - x[k])
#     #        n         (k≠i)            
#     # P(x) = Σ y[i] * ----------------- 
#     #       i=0         Π(x[i] - x[k])     
#     #                  (k≠i)
#     #        n                                              
#     #      = Σ Q[i] * Π(x - x[k])
#     #       i=0      (k≠i)         
#     #
#     #
#     #        n         (x - x[0])(x - x[1])・・・(x - x[k])
#     #      = Σ Q[i] * -------------------------------------
#     #       i=0                     (x - x[i])
#     #
#     #        n             R
#     #      = Σ Q[i] * ------------
#     #       i=0        (x - x[i])
#     #
#     #
#     #
#     #
#     N = len(points)

#     #
#     #               y[i]
#     # Q[i] = ------------------ : ラグランジュ補間公式におけるi項目のQ[i]。i番目の点(points[i])に関する項 (iは0-indexed)
#     #          Π(x[i] - x[k])
#     #         (k≠i)
#     #
#     Q = []
#     for i in range(N):
#         x_i, y_i = points[i]
#         denominator = 1
#         for k in range(N):
#             x_k, y_k = points[k]
#             if i == k:
#                 continue
#             denominator *= x_i - x_k
#             denominator %= MOD
#         Q.append(modinv(denominator, MOD) * y_i % MOD)
#     # print(Q)
#     #
#     # DP的に求める。
#     # R[i] = Π(x - x[i]) := i項目まで掛けた(たすき掛けした)時のx^jの係数はR[i][j] (mod MOD) 
#     # ※ 便宜上i=0はどの項も選択されていない状態でR[0]=定数1とする。
#     #
#     # R[i + 1] = R[i] * (x - x[i + 1]) の漸化式なのでDP的に解く。
#     #
#     # なお、全てのiについて結果を保持しておく必要がないのでここではRを二次元配列にせずR = calcedRとして上書きし、末尾にあたるR[-1]のみを持つようにしている。
#     #
#     R = [1] + [0] * N # 定数c = 1のみの項。
#     for i in range(N): # i項目の (x - x[i])を掛けた後の係数を算出する。
#         x_i, y_i = points[i]
#         calcedR = [0] * (N + 1)
#         # x^jの係数にたすき掛け。
#         # (・・多項式・・) * (x - x[i + 1]) の定数側の係数(-x[i + 1])を掛ける処理
#         for j in range(N):
#             calcedR[j] += -x_i * R[j]
#             calcedR[j] %= MOD
#         # (・・多項式・・) * (x - x[i + 1]) のx側の係数(1)を掛ける処理
#         for j in range(N):
#             calcedR[j + 1] += 1 * R[j]
#             calcedR[j + 1] %= MOD
#         R = calcedR

#     # P(x)の各項の係数を算出する。
#     #          n
#     #  P(x) =　Σ Q[i] * Π(x - x[k]) = 
#     #         i=0      (k≠i)
#     coef = [0] * N
#     for i in range(N):
#         x_i, y_i = points[i]
#         if Q[i] == 0:
#             continue
#         if x_i == 0: 
#             # (x - 0)の項 すなわち x で割るので全ての係数を1つ落としたものを加えたらいい。 R[j] → R[j + 1]を使用。
#             # この分岐処理をなくしてelse以下と同じ処理をしてもいいがそのままだとpow(0, -1)が死ぬので注意。
#             for j in range(N):
#                 coef[j] += R[j + 1] * Q[i] % MOD
#                 coef[j] %= MOD
#         else:
#             # (x - x_i)の項 すなわち (x - x_i) で割る。 (x_i ≠ 0)
#             # P(x)の定数項は -x_i にのみ影響されるので -x_i で割るのみ。
#             pre = -R[0] * modinv(x_i, MOD) % MOD
#             coef[0] += pre * Q[i] % MOD
#             coef[0] %= MOD
#             # P(x)のx^jの係数の項は 尻からやってる 汎用的にするなら前からの方がいいのでは
#             for j in range(1, N):
#                 nex = -(R[j] - pre) * modinv(x_i, MOD) % MOD
#                 coef[j] += nex * Q[i] % MOD
#                 coef[j] %= MOD
#                 pre = nex
#     return coef
