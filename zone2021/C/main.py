#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]", E: "List[int]"):
    # True ------ ok | ng ---- False
    def is_ok(k: int):
        s = set()
        for aa, bb, cc, dd, ee in zip(A, B, C, D, E):
            l = [aa, bb, cc, dd, ee]
            bit = 0
            for i in range(5):
                if l[i] >= k:
                    bit += 2 ** i
            s.add(bit)
            for x in s:
                for y in s:
                    for z in s:
                        if x | y | z == 31:
                            return True
        return False

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

    ans = binSearch(0, 10 ** 9 + 1)
    print(ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    C = [int()] * (N)  # type: "List[int]"
    D = [int()] * (N)  # type: "List[int]"
    E = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
        E[i] = int(next(tokens))
    solve(N, A, B, C, D, E)

if __name__ == '__main__':
    main()
