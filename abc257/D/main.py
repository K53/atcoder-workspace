#!/usr/bin/env python3
import sys
from collections import deque
INF = 10 ** 16

def solve(N: int, x: "List[int]", y: "List[int]", P: "List[int]"):
    def bfs(start_node: int, ss) -> list:
        q = deque()
        seen = [INF] * N
        q.append(start_node)
        seen[start_node] = 1
        while q:
            now = q.popleft()
            for next in range(N):
                if seen[next] != INF:
                    continue
                if abs(x[now] - x[next]) + abs(y[now] - y[next]) <= P[now] * ss:
                    q.append(next)
                    seen[next] = 1
        return seen

    # True ------ ok | ng ---- False
    def is_ok(ss: int):
        for start in range(N):
            seen = bfs(start, ss)
            if INF not in set(seen):
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

    ans = binSearch(INF, -1)
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
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        P[i] = int(next(tokens))
    solve(N, x, y, P)

if __name__ == '__main__':
    main()
