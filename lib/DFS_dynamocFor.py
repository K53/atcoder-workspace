#!/usr/bin/env python3
# https://atcoder.jp/contests/abc233/tasks/abc233_c
import sys
sys.setrecursionlimit(10 ** 9)

def main():
    N, X = map(int, input().split())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split())))
    ans = 0
    def dfs(depth: int, acc: int):
        nonlocal ans
        # --- 探索終了条件 ----------------------------
        if depth >= N:
            if acc == X:
                ans += 1
            return
        # --- 次の探索(分岐) --------------------------
        for a in l[depth][1:]:
            dfs(depth + 1, acc * a)
        return
    dfs(0, 1)
    print(ans)


if __name__ == '__main__':
    main()
