#!/usr/bin/env python3
import sys

def main():
    n = int(input())
    # True ------ ok | ng ---- False
    def is_ok(k: int):
        return k * (k + 1) // 2 <= n + 1
    
    def binSearch(ok: int, ng: int):
        # print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            # print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ok        

    print(n - binSearch(0,n+1) + 1)

if __name__ == '__main__':
    main()
