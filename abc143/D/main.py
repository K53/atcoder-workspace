#!/usr/bin/env python3
import sys


def solve(N: int, L: "List[int]"):
    L.sort(reverse=True)
    # True -- ok | ng -- Flase
    def is_ok(ci: int, bi: int, ai: int):
        if ci <= bi: return False
        if ci >= N: return True
        return abs(L[ai] - L[bi]) < L[ci] < L[ai] + L[bi]

    def binSearch(ok: int, ng: int, bi: int, ai: int):
        # print(ok, ng)              # はじめの2値の状態
        while abs(ok - ng) > 1:     # 終了条件（差が1となり境界を見つけた時)
            mid = (ok + ng) // 2
            if is_ok(mid, bi, ai):
                ok = mid            # midが条件を満たすならmidまではokなのでokの方を真ん中まで持っていく
            else:
                ng = mid            # midが条件を満たさないならmidまではngなのでngの方を真ん中まで持っていく
            # print(ok, ng)          # 半分に切り分ける毎の2値の状態
        return ok

    ans = 0
    # print(L)
    for ai in range(N - 2):
        for bi in range(ai + 1, N - 1):
            # print([L[ai], L[bi]])
            ci = binSearch(bi, N, bi, ai)
            ans += ci - bi
    print(ans)            
    return

# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, L)

if __name__ == '__main__':
    main()
