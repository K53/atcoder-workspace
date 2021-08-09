#!/usr/bin/env python3
import sys

def solve(R: int, B: int, x: int, y: int):
    def is_ok(k: int):
        rr = R - k
        bb = B - k
        return rr >= 0 and bb >= 0 and (rr // (x - 1) + bb // (y - 1)) >= k

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
        return ok   
    print(binSearch(-1, 10 ** 18 + 1)) 
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    R = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    x = int(next(tokens))  # type: int
    y = int(next(tokens))  # type: int
    solve(R, B, x, y)

if __name__ == '__main__':
    main()
