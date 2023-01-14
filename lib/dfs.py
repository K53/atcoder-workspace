# ------------------------------------------------------------------------------
#     DFS (グラフ/グリッド)
# ------------------------------------------------------------------------------
# Order
#   O(V + E)
#
# イメージ
#             ◯   <-- pre
#             |
#             ◯   <-- now
#           / | \
#      [1]↓/  |  \
#         /   |   \
#        /    |    \
#       /↑[4] |     \
#   ↓  /      |      \
#  [2]◯[3]    ◯       ◯ <-- next
#
# verify
# - https://atcoder.jp/contests/abc036/tasks/abc036_d (グラフ/木)
# - https://atcoder.jp/contests/abc233/tasks/abc233_c (他 : 一方向性の組み合わせ)
# - https://atcoder.jp/contests/atc001/tasks/dfs_a (グリッド)
# ------------------------------------------------------------------------------
# グラフ
import sys
sys.setrecursionlimit(10 ** 9)

N = 10
G = [[] for _ in range(N)] # 隣接リスト

seen = [0] * N
def dfs(pre: int, now: int):
    # print(pre, now)
    # [2] 
    # そのノードに初めて到着した時のみ
    # <<== 行きがけ順ならここを使う (初めて降り立つ時にしか実行されない)
    seen[now] = 1 # 訪問済みにする #開始点もseenにしないといけないのでfor前にフラグを立てる。
    # --- 子ノードを探索 -----------------------
    for next in G[now]: 
        # --- 遷移前に訪問済みチェック ----------- # 木であれば "next == pre" で判定でも可
        if seen[next] == 1: 
            continue
        # [1]
        # そのノードから子ノードに向かって出発しようとした時
        dfs(now, next)
        # [4]
        # そのノードに子ノードから帰ってきて到着した時
        # <== 木上のDPをする時はここを使うこと。
        # <== 領域[3]を使うと子から帰る時に親を操作するようになり直感に反する(あと1頂点のみのケースとかで例外処理が面倒)。
    # [3]
    # そのノードから親ノードに帰ろうと出発した時
    # <<== 帰りがけ順ならここを使う
    return

## ======================================================================================
# グリッド
import sys
sys.setrecursionlimit(10 ** 9)

H, W = 1, 1
G = []
seen = []
for _ in range(H):
    G.append(input())
    seen.append([False] * W)

def dfs(now_y: int, now_x: int):
    # print(pre, now)
    # [2]
    seen[now_y][now_x] = 1
    # --- 子ノードを探索 -----------------------
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next_y = now_y + dy
        next_x = now_x + dx
        if next_x < 0 or next_y < 0 or next_x >= W or next_y >= H or G[next_y][next_x] == "#" or seen[next_y][next_x]:
            continue
        # [1]
        dfs(next_y, next_x)
        # [4]
    # [3]
    return



## ======================================================================================
## グラフ以外の例題
# 一方向性なのでdepthを渡して行く。

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
        for num in l[depth]:
            if depth + 1 == N:
                if acc * num == X:
                    ans += 1
            else:
                dfs(depth + 1, acc * num)
        return

    dfs(0, 1)
    print(ans)


# from functools import lru_cache
# @lru_cache(maxsize=7000)