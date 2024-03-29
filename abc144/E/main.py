#!/usr/bin/env python3
import sys


def solve(N: int, K: int, A: "List[int]", F: "List[int]"):
    A.sort()
    F.sort()
    # True ------ ok | ng ---- False
    def is_ok(m: int):
        k = 0
        for i in range(N):
            k += max(0, A[i] -  m // F[-1 - i])
        return k <= K

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

    print(binSearch(10 ** 12 + 1, -1))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    F = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, K, A, F)

if __name__ == '__main__':
    main()
