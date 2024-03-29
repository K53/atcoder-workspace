#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

MOD = 1000000007  # type: int
from collections import deque

def solve(N: int, x: "List[int]", y: "List[int]"):
    # dp[now][color] := ノードnowを根とした部分木において、ノードnowを色colorで塗る場合の数。
    # 根において分岐がある場合、それらの総積で更新される。なので配列の初期値は1。
    # dp[now] = dp[next1] * dp[next2] * ...
    #      [now]
    #      /   \
    # [next1] [next2]
    #
    # ここで色を考慮すると、
    # nowを白に塗るなら他のノードは関係ないので、dp[now][白] = (dp[next1][白]＋ dp[next1][黒]) * (...) * ...
    # nowを黒に塗るなら隣は白いノードである必要があるため dp[now][黒] = dp[next1][白] * dp[next2][白] * ...

    dp = [[1] * 2 for _ in range(N)]
    G = [[] for _ in range(N)]
    for xx, yy in zip(x, y):
        G[xx - 1].append(yy - 1)
        G[yy - 1].append(xx - 1)

    def dfs(now: int, pre: int):
        for next in G[now]:
            if next == pre:
                continue
            dfs(next, now)
            dp[now][0] *= dp[next][0] + dp[next][1]
            dp[now][1] *= dp[next][0]
            dp[now][0] %= MOD
            dp[now][1] %= MOD
        return

    dfs(0, -1)
    print(sum(dp[0]) % MOD)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N - 1)  # type: "List[int]"
    y = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)

if __name__ == '__main__':
    main()
