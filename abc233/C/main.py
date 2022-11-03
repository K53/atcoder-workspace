#!/usr/bin/env python3
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
        # print(depth, acc)
        # --- 子ノードを探索 -----------------------
        for num in l[depth][1:]:
            if depth + 1 == N:
                if acc * num == X:
                    ans += 1
            else:
                dfs(depth + 1, acc * num)
        return

    dfs(0, 1)
    print(ans)


if __name__ == '__main__':
    main()
