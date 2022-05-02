


# https://atcoder.jp/contests/abc213/submissions/24899201
# https://hcpc-hokudai.github.io/archive/graph_tree_001.pdf


# 隣接リスト
G = [[1, 2], [0, 3], [0], [1]]
# グラフ イメージ
#  (2) - (0) - (1) - (3)

# 頂点に関するオイラーツアー
import sys
eularTourNodes_pattarnA = []
eularTourNodes_pattarnB = []
sys.setrecursionlimit(10 ** 9)
def getEularTourNodes(now: int, pre: int = -1):
    eularTourNodes_pattarnA.append(now) # ノードから葉の方へ出る時に記録
    eularTourNodes_pattarnB.append(now) # ノードから葉の方へ出る時に記録
    for next in G[now]:
        if next == pre:
            continue
        getEularTourNodes(next, now) 
        eularTourNodes_pattarnA.append(now) # ノード経由時に記録 (Path.A)
    eularTourNodes_pattarnB.append(now) # ノードから根に戻る時に記録 (Path.B)
    return
getEularTourNodes(0)
print("-----")
print("eularTourNodes_pattarnA", eularTourNodes_pattarnA)
print("eularTourNodes_pattarnB", eularTourNodes_pattarnB)
print("-----")

