# ------------------------------------------------------------------------------
#     二分探索 (Binary Search)
# ------------------------------------------------------------------------------
# verify
#  - https://yukicoder.me/submissions/759180 (ok/ngを反転するケース)
# ------------------------------------------------------------------------------

# True ------ ok | ng ---- False
def is_ok(k: int):
    return k * (k + 1) // 2 <= n + 1    # 条件式

def binSearch(ok: int, ng: int):
    # print(ok, ng)              # はじめの2値の状態
    while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
        mid = (ok + ng) // 2
        # print("target > ", mid)
        result = is_ok(mid)
        # print(result)
        if result:
            ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
        else:
            ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
        # print(ok, ng)          # 半分に切り分ける毎の2値の状態
    return ok    # 関数呼び出し時の引数のngは絶対評価されないのでngに書く値が答えになりうるならその数マイナス1を指定する。
