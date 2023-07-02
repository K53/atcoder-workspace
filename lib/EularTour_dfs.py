# ------------------------------------------------------------------------------
#     オイラーツアー (DFS版)
# ------------------------------------------------------------------------------
# Order
#   O(V + E)
#
# Point!
# - forブロックの外のnowは、ブロック内のnext。
#
#
# 参考
# - https://hcpc-hokudai.github.io/archive/graph_tree_001.pdf
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
# - https://atcoder.jp/contests/abc213/tasks/abc213_d (グラフ/木)
# ------------------------------------------------------------------------------


# 隣接リスト
G = [[1, 2], [0, 3], [0], [1]]
# グラフ イメージ
#      (0)
#    /     \
#  (2)     (1)
#           |
#          (3)

# 頂点に関するオイラーツアー
import sys
sys.setrecursionlimit(10 ** 9)

eularTourNodes_pattarnA = []
eularTourNodes_pattarnB = []
def getEularTourNodes(now: int, pre: int = -1):
    # [2] 
    # そのノードに初めて到着した時のみ
    eularTourNodes_pattarnA.append(now) 
    eularTourNodes_pattarnB.append(now)
    for next in G[now]:
        if next == pre:
            continue
        # [1]
        # そのノードから子ノードに向かって出発しようとした時
        getEularTourNodes(next, now) 
        # [4]
        # そのノードに子ノードから帰ってきて到着した時
        eularTourNodes_pattarnA.append(now)
    # [3]
    # そのノードから親ノードに帰ろうと出発した時
    eularTourNodes_pattarnB.append(now)
    return
getEularTourNodes(0)
print("-----")
print("eularTourNodes_pattarnA", eularTourNodes_pattarnA)
print("eularTourNodes_pattarnB", eularTourNodes_pattarnB)
print("-----")

# 出力
# -----
# eularTourNodes_pattarnA [0, 1, 3, 1, 0, 2, 0]
# eularTourNodes_pattarnB [0, 1, 3, 3, 1, 2, 2, 0]
# -----

# [2]のタイミングでのみ記録を取ると、初めてそのノードに到着した瞬間しか記録できないので、初めて訪問したノードの順が得られる。
# ここに、子から戻ってくるたびにも記録したいのであれば、子から帰ってきて到着した瞬間を示す[3]のタイミングでも記録をするべきとわかる。
# => eularTourNodes_pattarnA 
#
# なお、帰ろうとする時の出発時に記録をすると、初めての到着時と毎回の出発時で2回記録される瞬間が出現するのでおかしなことになる。

## 以下は調査・検証用

# ==================================
eularTourNodes_pattarnA = []
eularTourNodes_pattarnB = []
eularTourNodes_pattarnC = []
eularTourNodes_pattarnD = []
def getEularTourNodes(now: int, pre: int = -1):
    # [2]
    eularTourNodes_pattarnA.append(now) # ノードから葉の方へ出る時に記録
    eularTourNodes_pattarnB.append(now) # ノードから葉の方へ出る時に記録
    for next in G[now]:
        if next == pre:
            continue
        # [1]
        eularTourNodes_pattarnC.append(next) # ノードから葉の方へ出る時に記録
        eularTourNodes_pattarnD.append(next) # ノードから葉の方へ出る時に記録
        getEularTourNodes(next, now) 
        #[4]
        eularTourNodes_pattarnA.append(now) # ノード経由時に記録 (Path.A)
        eularTourNodes_pattarnC.append(now) # ノード経由時に記録 (Path.C)
    # [3]
    eularTourNodes_pattarnB.append(now) # ノードから根に戻る時に記録 (Path.B)
    eularTourNodes_pattarnD.append(now) # ノードから根に戻る時に記録 (Path.D)
    return
getEularTourNodes(0)
print("-----")
print("eularTourNodes_pattarnA", eularTourNodes_pattarnA)
print("eularTourNodes_pattarnB", eularTourNodes_pattarnB)
print("eularTourNodes_pattarnC", eularTourNodes_pattarnC)
print("eularTourNodes_pattarnD", eularTourNodes_pattarnD)
print("-----")

# 出力
# -----
# eularTourNodes_pattarnA [0, 1, 3, 1, 0, 2, 0]
# eularTourNodes_pattarnB [0, 1, 3, 3, 1, 2, 2, 0]
# eularTourNodes_pattarnC [1, 3, 1, 0, 2, 0]
# eularTourNodes_pattarnD [1, 3, 3, 1, 2, 2, 0]
# -----

# => まとめ1: 領域1にnowとしておくか、領域2にnextで置くかは、先頭要素を出力に加えたいかどうかにのみ影響する。
# => 重複して一つの頂点の記録をしたくない場合、forの外でnowを中でnextを打刻する組み合わせにしないこと

# =================================================================================================

eularTourNodes_pattarnA = []
eularTourNodes_pattarnA2 = []
eularTourNodes_pattarnB = []
eularTourNodes_pattarnC = []
eularTourNodes_pattarnD = []
def getEularTourNodes(now: int, pre: int = -1):
    # [2]
    eularTourNodes_pattarnA.append(now) # ノードから葉の方へ出る時に記録 @Node
    eularTourNodes_pattarnA2.append(now) # ノードから葉の方へ出る時に記録 @Node
    eularTourNodes_pattarnB.append(now) # ノードから葉の方へ出る時に記録 @Node
    for next in G[now]:
        if next == pre:
            continue
        # [1]
        eularTourNodes_pattarnC.append(next) # ノードから葉の方へ出る時に記録 @Edge
        eularTourNodes_pattarnD.append(next) # ノードから葉の方へ出る時に記録 @Edge
        getEularTourNodes(next, now) 
        #[4]
        eularTourNodes_pattarnA.append(next + 10) # ノード経由時に記録 (Path.A) @Edge
        eularTourNodes_pattarnA2.append(now) # ノード経由時に記録 (Path.A) @Edge
        eularTourNodes_pattarnC.append(now) # ノード経由時に記録 (Path.C) @Edge
    # [3]
    eularTourNodes_pattarnB.append(now) # ノードから根に戻る時に記録 (Path.B) @Node
    eularTourNodes_pattarnD.append(now) # ノードから根に戻る時に記録 (Path.D) @Node
    return
getEularTourNodes(0)
print("-----")
print("eularTourNodes_pattarnA", eularTourNodes_pattarnA)
print("eularTourNodes_pattarnA2", eularTourNodes_pattarnA2)
print("eularTourNodes_pattarnB", eularTourNodes_pattarnB)   # 折り返しを考えるとわかるが、このケースは折り返し時に同じ数字が重複する
print("eularTourNodes_pattarnC", eularTourNodes_pattarnC)
print("eularTourNodes_pattarnD", eularTourNodes_pattarnD)
print("-----")


# 出力
# -----
# eularTourNodes_pattarnA [0, 1, 3, 13, 11, 2, 12]
# eularTourNodes_pattarnA2 [0, 1, 3, 11, 10, 2, 10]
# eularTourNodes_pattarnB [0, 1, 3, 3, 1, 2, 2, 0]
# eularTourNodes_pattarnC [1, 3, 1, 0, 2, 0]
# eularTourNodes_pattarnD [1, 3, 3, 1, 2, 2, 0]
# -----

# => まとめ1: 領域3でのnextの記録は領域1のnowの記録と重複する。これは 1はnow到着時の記録。3はnextから帰還時の記録。
# => まとめ2: 領域4でのnowの記録はnowから帰還時の記録になる。そのため領域3のnextは領域4でのnowと同じ結果を得る。
# => まとめ3: for内(領域1or3)のnextの記録では根まで戻ってきた時に記録されない。領域4のnowではされる。
