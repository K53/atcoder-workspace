#!/usr/bin/env python3
import sys
MOD = 998244353
input = sys.stdin.readline

def main():
    A, B, N, M = map(int, input().split())
    # False ------ ng | ok ---- True
    def is_ok(k: int):
        if A >= k:
            return B + (A - k) // N >= k
        elif B >= k:
            return A + (B - k) // M >= k
        return False

    def binSearch(ng: int, ok: int):
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
        return ok  

    print(binSearch(10 ** 18 + 1, 0))
    return

if __name__ == '__main__':
    main()