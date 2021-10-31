


# https://atcoder.jp/contests/abc213/submissions/24899201
# https://hcpc-hokudai.github.io/archive/graph_tree_001.pdf


# 頂点に関するオイラーツアー
import sys
eularTourNodes = []
sys.setrecursionlimit(10 ** 9)
def getEularTourNodes(now: int, pre: int = -1):
    eularTourNodes.append(now)
    for next in nodes[now]:
        if next == pre:
            continue
        getEularTourNodes(next, now)
        eularTourNodes.append(now)
    return
getEularTourNodes(0)