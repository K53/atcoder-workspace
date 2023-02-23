#!/usr/bin/env python3
import sys
from decimal import Decimal
INF = 10 ** 6
# https://marco-note.net/abc-191-work-log/
# 解説AC

# Z^2 = R^2 - (y -original_y)^2
# (x - original_x)^2 <= Z^2
# -> original_x - Z <= x <= original_x + Z

def main():
    offset = 10 ** 4
    X, Y, R = map(lambda x: int(Decimal(x) * offset), input().split())
    ans = 0
    original_x = X // offset
    # True ------ ok | ng ---- False
    def is_ok(k: int, Z2):
        return (k - X) ** 2 <= Z2

    def binSearch(ok: int, ng: int, Z2):
        # print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            # print("target > ", mid)
            result = is_ok(mid, Z2)
            # print(result)
            if result:
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            # print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ok    # 関数呼び出し時の引数のngは絶対評価されないのでngに書く値が答えになりうるならその数マイナス1を指定する。

    for targeted_Y in range(((Y - R) // offset * offset), (Y + R) + offset, offset):
        Z2 = R ** 2 - (targeted_Y - Y) ** 2
        if Z2 < 0:
            # 交点なし
            continue
        if (X - (original_x * offset)) ** 2 <= Z2:
            # print(targeted_Y, "#")
            min_X = binSearch(X, -INF, Z2)
            if min_X < 0:
                min_X = -(-min_X // offset) * offset
            else:
                min_X = min_X // offset * offset
            cnt = (X - min_X) // offset + 1
            # print(cnt)
            ans += cnt

        #   -------------------------->
        #     l    l    l    l    l
        #               of k
        if (X - (original_x * offset + offset)) ** 2 <= Z2:
            # print(targeted_Y, "S")
            t = binSearch(X + 1, INF, Z2) 
            max_X = t // offset
            # print(t, max_X, original_x + 1)
            if max_X == original_x:
                cnt= 1
            else:
                cnt = max_X - (original_x + 1) + 1
            # print(cnt)
            ans += cnt
    print(ans)
    return

if __name__ == '__main__':
    main()
