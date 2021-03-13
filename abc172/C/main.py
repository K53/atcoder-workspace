#!/usr/bin/env python3
import sys
import itertools

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Sa = [0] + sorted(list(itertools.accumulate(A)))
    Sb = [0] + sorted(list(itertools.accumulate(B)))

    # True ---- ok | ng ---- False
    def is_ok(mid: int, sa: int):
        # 検索対象の外にあるものは先に弾く(リストのインデックスなんかだとout of rangeするので)
        if mid < 0:
            return True
        elif mid > len(Sb):
            return False
        return sa + Sb[mid] <= K

    def binSearch(ok: int, ng: int, sa: int):
        #print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            if is_ok(mid, sa):
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            #print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ok                   # 取り出すのは基本的にokの方。(問題によりけり)
    
    ans = 0
    for n in range(N + 1):
        num = binSearch(-1, M + 1, Sa[n])
        if num < 0:
            continue
        ans = max(ans, n + num)
    print(ans)



if __name__ == '__main__':
    main()
