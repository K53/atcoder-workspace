#!/usr/bin/env python3
from itertools import combinations
import sys


# True ------ ok | ng ---- False
def is_ok(s: int, k: int):
    print("? 1 N", s, k, flush=True)
    return int(input()) == k - s + 1

def binSearch(ok: int, ng: int):
    l = 0
    # print(ok, ng)              # はじめの2値の状態
    while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
        mid = (ok + ng) // 2
        # print("target > ", mid)
        if l == 0:
            result = is_ok(ok, mid)
        else:
            result = is_ok(mid, ng)
        # print(result)
        if result:
            ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            l = 1
        else:
            ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            l = 0
        # print(ok, ng)          # 半分に切り分ける毎の2値の状態
    return ok    # 関数呼び出し時の引数のngは絶対評価されないのでngに書く値が答えになりうるならその数マイナス1を指定する。
# True ------ ok | ng ---- False
def is_ok2(s: int, k: int):
    print("?", s, k, "1 N", flush=True)
    return int(input()) == k - s + 1

def binSearch2(ok: int, ng: int):
    l = 0
    # print(ok, ng)              # はじめの2値の状態
    while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
        mid = (ok + ng) // 2
        # print("target > ", mid)
        if l == 0:
            result = is_ok2(ok, mid)
        else:
            result = is_ok2(mid, ng)
        # print(result)
        if result:
            ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            l = 1
        else:
            ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            l = 0
        # print(ok, ng)          # 半分に切り分ける毎の2値の状態
    return ok    # 関数呼び出し時の引数のngは絶対評価されないのでngに書く値が答えになりうるならその数マイナス1を指定する。


def solve(N: int):
    a = binSearch(0, N)
    b = binSearch(0, N)
    print(a, b, flush=True)


    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    X = int(next(tokens))  # type: int
    solve(X)

if __name__ == '__main__':
    main()
