# ------------------------------------------------------------------------------
#     LowLink (グラフの橋と関節点の算出)
# ------------------------------------------------------------------------------
# 解説
# 無向グラフにおいて橋、関節点のリストを取得する。
#
# リンク
# https://algo-logic.info/bridge-lowlink/#
# 
# 計算量
# - O(V + E) : 要するに2回のDFSなので。
# 
# verify
# - https://atcoder.jp/contests/abc075/tasks/abc075_c
# ------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(10 ** 9)
class Lowlink():
    def __init__(self, N: int) -> None:
        self.N = N
        self.G = [[] for _ in range(self.N)]                    # 与えられたグラフ
        self.seen = [False] * self.N                            # 各ノードが訪問済みかどうかのフラグ
        self.first_order = [-1] * self.N                         # 各ノードの行きがけ順
        self.lowlink = [-1] * self.N                            # 各ノードがどのグループに属するか
        self.bridges = []                                       # 橋のリスト
        self.artification_points = []                           # 関節点のリスト

    def addEdge(self, fromNode: int, toNode: int):
        # print("Really directed Graph?")
        self.G[fromNode].append(toNode)
        return
    
    # DFS
    def _dfs(self, node_num: int, cur_node: int, prev_node: int):
        self.seen[cur_node] = True
        self.first_order[cur_node] = node_num
        self.lowlink[cur_node] = self.first_order[cur_node]
        node_num += 1
        is_artification_points = False
        child_count = 0 # その親からの子ノードの数。※親は1個。 三角形のような閉じた図形の場合child_nodeは末端は0、それ以外は1ずつ。2とはならない。
        for next_node in self.G[cur_node]:
            if next_node == prev_node: # 後退辺(親に戻る辺)なら弾く
                continue
            if not self.seen[next_node]:
                child_count += 1
                node_num = self._dfs(node_num, next_node, cur_node) 
                self.lowlink[cur_node] = min(self.lowlink[cur_node], self.lowlink[next_node]) # DFSで末端から帰ってくる時に末端側でサイクルがあってlowlinkに変更があったならこちらも影響するか確認。
                if self.first_order[cur_node] < self.lowlink[next_node]:
                    self.bridges.append((min(cur_node, next_node), max(cur_node, next_node)))
                if prev_node != -1 and self.first_order[cur_node] <= self.lowlink[next_node]:
                    is_artification_points = True
            # 後退辺でないのに既に訪問済みなのは閉路だからとわかる。
            self.lowlink[cur_node] = min(self.lowlink[cur_node], self.first_order[next_node])
        if prev_node == -1 and child_count >= 2: # 親が端なら関節点ではないが、二股になってるなら関節点。
            is_artification_points = True
        if is_artification_points:
            self.artification_points.append(cur_node)
        return node_num

    def build(self) -> None:
        """ 
        橋、関節点のリストを生成。
        O(V + E) ← 要するにDFSなので
        """
        # 初めから全頂点が連結でない場合を考慮
        for start_node in range(self.N):
            if self.seen[start_node]:
                continue
            self._dfs(0, start_node, -1)
        return

# Usage
N = 7
A = [1, 2, 3, 4, 4, 5, 6]
B = [3, 7, 4, 5, 6, 6, 7]
#
#                [5]
#               /   \
# [1] - [3] - [4] - [6] - [7] - [2]
#
ll = Lowlink(N)
for aa, bb in zip(A, B):
    ll.addEdge(aa - 1, bb - 1)
    # ll.addEdge(bb - 1, aa - 1)
ll.build()

print(ll.bridges) # 橋 : その辺を失うとグラフが連結でなくなる辺。
# -> [(1, 6), (5, 6), (2, 3), (0, 2)]
print(ll.artification_points)
# -> [6, 5, 3, 2] # 関節点 : そのノードを失うとグラフが連結でなくなるノード。
print(ll.lowlink) 
# -> [0, 6, 1, 2, 2, 2, 5] # 同一のサイクルに含まれているノードには同じ番号が書かれている。
    