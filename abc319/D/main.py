#!/usr/bin/env python3





def main():
    N, M = map(int, input().split())
    L = list(map(int, input().split()))
    def getRow(width):
        acc = 0
        line = 1
        for i in range(N):
            ll = L[i]
            if i == N - 1:
                if ll + acc <= width:
                    acc += ll
                else:
                    acc = ll
                    line += 1
            else:
                if ll + acc < width:
                    acc += ll + 1 # space
                elif ll + acc == width:
                    acc = 0
                    line += 1
                else:
                    acc = ll + 1
                    line += 1
        # print(line, acc)
        return line
    
    maxL = max(L)
    # ng False | True ok
    def is_ok(k: int):
        if k < maxL:
            return False
        return getRow(k) <= M

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


    print(binSearch(10 ** 15, 0))
    return
    



if __name__ == '__main__':
    main()
