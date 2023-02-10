#!/usr/bin/env python3
import sys
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


def solve(p: int, a: "List[int]"):
    [(i, aa) for i, aa in enumerate(a)]
    print(*lagrangeInterpolation([(i, aa) for i, aa in enumerate(a)], p))
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    p = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(p - 1 - 0 + 1)]  # type: "List[int]"
    solve(p, a)

if __name__ == '__main__':
    main()
