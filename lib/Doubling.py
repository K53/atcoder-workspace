# ------------------------------------------------------------------------------
#     ダブリング
# ------------------------------------------------------------------------------
# 解説
# - 特になし
# 
# リンク
# - ノーマルなダブリング→ https://qiita.com/Kept1994/items/ea91c057b0e552323da3
# - 総和のダブリング→ https://qiita.com/Kept1994/items/fa3917f2812f1a3f5f96
# 
# 計算量
# - O(HW) : テーブルのサイズに依存
# 
# Modify
# - https://yukicoder.me/problems/no/1595
# ------------------------------------------------------------------------------
class Doubling:
    """ 初期化処理。
    Parameters:
    ----------
    stateKind : int
        状態の数。dvテーブルの横の長さ。
    maxDoublingTimes : int
        ダブリングの回数。dvテーブルの縦の長さ。
    useSum : bool
        和のダブリングを使用するモードの選択。
    Returns:
    ----------
    None
    """
    def __init__(self, stateKind: int, maxDoublingTimes: int, useSum: bool = False):
        self.dv = []                                # 数列(状態)のダブリングテーブル。dv[k][s] := 状態sを2^k回実行したらあとの状態
        self.sum = []                               # 和のダブリングテーブル
        self.stateKind = stateKind                  # 状態の種類数s
        self.maxDoublingTimes = maxDoublingTimes    # 実行回数kの範囲の定義(2^0 ≦ k ≦ 2^maxDoublingTimes)
        # --- Initialize -------------------
        # STEP.1 テーブルの初期化 2^0(=1)回操作後の状態を生成。
        self._initTable()
        # STEP.2 テーブルの更新。
        if useSum:
            self._createTableWithSum()
        else:
            self._createTable()
        # ---------------------------------

    # 初期化処理
    # 初期化処理は問題毎に記述する。
    def _initTable(self):
        # l = []
        # for i in range(self.stateKind):
        #     l.append(i)
        # self.dv.append(l)
        pass

    # ダブリング実施(和を含まない)
    def _createTable(self):
        for i in range(1, self.maxDoublingTimes):
            l = []
            for j in range(self.stateKind):
                l.append(self.dv[i - 1][self.dv[i - 1][j]])
            self.dv.append(l)

    # ダブリング実施(和を含む)
    def _createTableWithSum(self):
        for i in range(1, self.maxDoublingTimes):
            l = []
            s = []
            for j in range(self.stateKind):
                l.append(self.dv[i - 1][self.dv[i - 1][j]])
                s.append(self.sum[i - 1][j] + self.sum[i - 1][self.dv[i - 1][j]])
            self.dv.append(l)
            self.sum.append(s)
    
    """ 指定回数操作後の状態を算出する。
    Parameters:
    ----------
    doubingTimes : int
        求める状態に至る操作回数。
    startState : int
        開始する状態。
    Returns:
    ----------
    int
        求めるべく状態
    """
    def getState(self, doubingTimes: int, startState: int):
        a = []
        for i in range(self.maxDoublingTimes):
            if doubingTimes >> i & 1:
                a.append(i)
        now = startState
        for i in a:
            now = self.dv[i][now]
        return now
    
    """
    """
    def getSum(self, doubingTimes: int, startState: int):
        res = 0
        a = []
        for i in range(self.maxDoublingTimes):
            if doubingTimes >> i & 1:
                a.append(i)
        now = startState
        for i in a:
            res += self.sum[i][now]
            now = self.dv[i][now]
        return res

    def getAllStates(self, targenTime: int):
        return self.dv[targenTime]

# Usage
import math
N = 100
K = 10 ** 18
d = Doubling(stateKind=N, maxDoublingTimes=int(math.log2(K)) + 1, useSum=False)
print(d.getState(doubingTimes=K, startState=0))