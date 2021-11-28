#!/usr/bin/env python3
from sys import stdin

def main():
    T = int(input())
    # True ------ ok | ng ---- False
    def is_ok(k: int, nn):
        return k ** 2 <= nn

    def binSearch(ok: int, ng: int, nn):
        # print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            # print("target > ", mid)
            result = is_ok(mid, nn)
            # print(result)
            if result:
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            # print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ok    # 関数呼び出し時の引数のngは絶対評価されないのでngに書く値が答えになりうるならその数マイナス1を指定する。

    for _ in range(T):
        N = int(input())
        ans = binSearch(1, 10 ** 9 + 1, N)
        print(ans)
    return
            

if __name__ == '__main__':
    main()