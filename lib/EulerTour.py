# ------------------------------------------------------------------------------
#     EulerTour (オイラーツアー : 部分木に対するクエリに回答できるデータ構造)
# ------------------------------------------------------------------------------
# 解説
# - 木に対するオイラーツアーを求め、その順でコストの和をセグ木で管理した。
# - 部分木に対するクエリに回答可能。
#
# リンク
# - https://qiita.com/recuraki/items/72e37eb9be9f71bc623a
#
# 計算量
# - build() 構築 O(V + E)
#   - オイラーツアー算出
#   - 行きがけ順算出
#   - 帰りがけ順算出
# - セグ木構築 O(4V)) : 以下のクエリには必要
# - getLca() :  LCA取得 O(log(2V))
#   - 前準備としてlcaBuild()の実施が必要
# - getPartialTreeVertexCost() : 部分木のノードコストの総和を取得 O(log(2V))
#   - 前準備としてvertexPosSumBuild()の実施が必要
# - getPartialTreeEdgeCost() : 部分木の辺のコストの総和を取得 O(log(2V))
#   - 前準備としてedgePosSumBuild()の実施が必要
# - getPathVertexCost() : 2点間のパスのノードコストの総和を取得 O(log(2V))
#   - 前準備としてvertexAllSumBuild(),lcaBuild()の実施が必要
# - getPathEdgeCost() : 2点間のパスの辺のコストの総和を取得 O(log(2V))
#   - 前準備としてedgeAllSumBuild(),lcaBuild()の実施が必要
# - updateVertexCost() : 任意のノードのコストを変更する。O(log(2V))
# - updateEdgeCost() : 任意の辺のコストを変更する。O(log(2V))
#
# verify
# - https://atcoder.jp/contests/abc213/submissions/43082386 (オイラーツアーの出力)
#
# maintain
# - 2023.07.01 : Created / Verified
# ===============================================================================
INF = 10 ** 16
from SegmentTree import SegTree

class EulerTour():
    def __init__(self, N: int, rootNode: int, vertexCosts: "list[int]" = None) -> None:
        self.N = N
        self.G = [[] for _ in range(self.N)]
        self.vertexCosts = vertexCosts if vertexCosts != None else [0] * self.N
        self.rootNode = rootNode

        self.eulerTourPath = []         # オイラーツアーパス
        self.eulerTourDepth = []        # オイラーツアーの各ノードの深さの遷移
        self.vertexCostsPosOnly = []    # ノードを遡上する際にコストを減算しない
        self.vertexCostsPosAndNeg = []  # ノードを遡上する際にコストを減算する
        self.edgeCostsPosOnly = []      # 辺を遡上する際にコストを減算しない
        self.edgeCostsPosAndNeg = []    # 辺を遡上する際にコストを減算する

        self.parent = [None] * self.N   # 各ノードの親ノード番号
        self.nodeDepth = [-1] * self.N  # 各ノードの根からの深さ (0-indexed)
        
        # nodeIn/nodeOut
        self.nodeIn = [-1] * self.N     # nodeIn[i]  := 根から何ステップでノードiに到着するか (nodeInとnodeOut合算してナンバリング)
        self.nodeOut = [-1] * self.N    # nodeOut[i] := 根から何ステップでノードiを出発するか (nodeInとnodeOut合算してナンバリング)
        
        self.preOrder = []
        self.postorderCount = [(-1, -1)] * self.N
        self.postOrder = []

        # SegTree
        self.segLca = None # LCA用
        self.segVertexPosSum = None # 部分木用(ノード)
        self.segEdgePosSum = None # 部分木用(辺)
        self.segVertexAllSum = None # パスクエリ用(ノード)
        self.segEdgeAllSum = None # パスクエリ用(辺)

    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((toNode, cost))
        print("Really directed Graph?")
        return

    def sortG(self):
        for i in range(N):
            self.G[i].sort()

    def build(self):
        """
        O(V + E)
        """
        curStep = 0
        # stack: (nodenum, depth, vcost, ecost)
        stack = [(self.rootNode, 0, 0, self.vertexCosts[self.rootNode])]
        while len(stack) > 0:
            curNode, curdepth, vcost, ecost = stack.pop()
            # 行きがけ処理
            if curNode >= 0:
                if self.nodeIn[curNode] == -1:
                    self.nodeIn[curNode] = curStep
                self.nodeDepth[curNode] = curdepth
                self.eulerTourPath.append(curNode)
                self.eulerTourDepth.append(curdepth)
                self.preOrder.append(curNode)
                self.edgeCostsPosOnly.append(vcost)
                self.edgeCostsPosAndNeg.append(vcost)
                self.vertexCostsPosOnly.append(ecost)
                self.vertexCostsPosAndNeg.append(ecost)

                # 葉である場合は帰りがけの処理もする
                if len(self.G[curNode]) == 1:
                    self.nodeOut[curNode] = curStep + 1
                    self.postorderCount[curNode] = (curStep, curNode)
                
                # stackなので隣接リストGの末尾から評価して詰めることでGの先端要素から取り出しできるようにしている。
                # 特に最小ノード番号からのオイラーツアーをするなら(=sortG()しているなら)恩恵がある。
                for nextnode, nextvcost in self.G[curNode][::-1]:
                    # if nextnode == self.parent[nextnode]: continue
                    # print("! ", nextnode, vcost)
                    if self.nodeDepth[nextnode] != -1:
                        continue
                    stack.append((~curNode, curdepth, nextvcost, -self.vertexCosts[nextnode]))
                    stack.append((nextnode, curdepth + 1, nextvcost, self.vertexCosts[nextnode]))
                    self.parent[nextnode] = curNode
            
            # 帰りがけ処理
            else:
                curNode = ~curNode
                if self.nodeIn[curNode] == -1:
                    self.nodeIn[curNode] = curStep
                self.nodeOut[curNode] = curStep + 1
                self.eulerTourPath.append(curNode)
                self.eulerTourDepth.append(curdepth)
                self.postorderCount[curNode] = (curStep, curNode)
                self.edgeCostsPosOnly.append(0)
                self.edgeCostsPosAndNeg.append(-vcost)
                self.vertexCostsPosOnly.append(0)
                self.vertexCostsPosAndNeg.append(ecost)

            # 次のStepへ
            curStep += 1

        # 最後の調整
        self.vertexCostsPosOnly.append(0)
        self.vertexCostsPosAndNeg.append(-self.vertexCosts[self.rootNode])
        self.edgeCostsPosOnly.append(0)
        self.edgeCostsPosAndNeg.append(0)
        self.postorderCount.sort()
        self.postOrder = [nodeNum for _, nodeNum in self.postorderCount]

    def lcaBuild(self):
        """
        LCA用のセグ木を構築
        O(4V)
        """
        def min_depth(a, b):
            return a if a[1] < b[1] else b
        self.segLca = SegTree((INF, INF), [(nodeNum, depth) for nodeNum, depth in zip(self.eulerTourPath ,self.eulerTourDepth)], min_depth)

    def vertexPosSumBuild(self):
        """
        部分木のノードコストの和算出用のセグ木を構築
        O(4V)
        """
        def add(a, b):
            return a + b
        self.segVertexPosSum = SegTree(0, self.vertexCostsPosOnly, add)
    
    def edgePosSumBuild(self):
        """
        部分木の辺のコストの和算出用のセグ木を構築
        O(4V)
        """
        def add(a, b):
            return a + b
        self.segEdgePosSum = SegTree(0, self.edgeCostsPosOnly, add)
    
    def vertexAllSumBuild(self):
        """
        パスクエリのノードコストの和算出用のセグ木を構築
        O(4V)
        """
        def add(a, b):
            return a + b
        self.segVertexAllSum = SegTree(0, self.vertexCostsPosAndNeg, add)
    
    def edgeAllSumBuild(self):
        """
        パスクエリの辺のコストの和算出用のセグ木を構築
        O(4V)
        """
        def add(a, b):
            return a + b
        self.segEdgeAllSum = SegTree(0, self.edgeCostsPosAndNeg, add)
    
    def getLca(self, a: int, b: int):
        """
        2点のノードの共通最小祖先(LCA)のノード番号を返却する。
        O(log(2V))
        input
            a: 1点目のノード番号 (0-indexed)
            b: 2点目のノード番号 (0-indexed)
        output
            lca_nodeNum: LCAノード番号
            (lca_depth : LCAノードの根からの深さ)
        """
        if self.segLca == None:
            print("you need call lcaBuild()")
            raise Exception("segLca is None")
        l = min(self.nodeIn[a], self.nodeIn[b])
        r = max(self.nodeOut[a], self.nodeOut[b])
        lca_nodeNum, lca_depth = self.segLca.getRange(l, r)
        return lca_nodeNum
    
    def getPartialTreeVertexCost(self, x: int):
        """
        ノードxを根とした部分木に属する全てのノードのコストの和を返却する。
        O(log(2V))
        input
            x: 根のノード番号 (0-indexed)
        output
            部分木のノードのコストの和
        """
        if self.segVertexPosSum == None:
            print("you need call vertexPosSumBuild()")
            raise Exception("segVertexPosSum is None")
        l = self.nodeIn[x]
        r = self.nodeOut[x]
        return self.segVertexPosSum.getRange(l, r)
    
    def getPartialTreeEdgeCost(self, x: int):
        """
        ノードxを根とした部分木に属する全ての辺のコストの和を返却する。
        O(log(2V))
        input
            x: 根のノード番号 (0-indexed)
        output
            部分木の辺のコストの和
        """
        if self.segEdgePosSum == None:
            print("you need call edgePosSumBuild()")
            raise Exception("segEdgePosSum is None")
        l = self.nodeIn[x] + 1
        r = self.nodeOut[x]
        return self.segEdgePosSum.getRange(l, r)

    def _getPathVertexCostFromRoot(self, x: int):
        """
        根からノードxまでのパスに含まれるノードのコストの和を返却する。
        O(log(2V))
        input
            x: 根のノード番号 (0-indexed)
        output
            根からノードxまでのノードのコストの総和
        """
        if self.segVertexAllSum == None:
            print("you need call vertexAllSumBuild()")
            raise Exception("segVertexAllSum is None")
        l = self.rootNode
        r = self.nodeIn[x] + 1
        return self.segVertexAllSum.getRange(l, r)

    def _getPathEdgeCostFromRoot(self, x: int):
        """
        根からノードxまでのパスに含まれる辺のコストの和を返却する。
        O(log(2V))
        input
            x: 根のノード番号 (0-indexed)
        output
            根からノードxまでの辺のコストの総和
        """
        if self.segEdgeAllSum == None:
            print("you need call edgeAllSumBuild()")
            raise Exception("segEdgeAllSum is None")
        l = self.rootNode
        r = self.nodeIn[x] + 1
        return self.segEdgeAllSum.getRange(l, r)

    def getPathVertexCost(self, a: int, b: int):
        """
        2点間のパスに含まれるノードのコストの和を返却する。
        O(log(2V))
        input
            a: 1点目のノード番号 (0-indexed)
            b: 2点目のノード番号 (0-indexed)
        output
            2点間のノードのコストの総和
        """
        if self.segVertexAllSum == None:
            print("you need call vertexAllSumBuild()")
            raise Exception("segVertexAllSum is None")

        lca = self.getLca(a, b)
        return self._getPathVertexCostFromRoot(a) + \
            self._getPathVertexCostFromRoot(b) - \
            self._getPathVertexCostFromRoot(lca) * 2 + \
            self.vertexCosts[lca]

    def getPathEdgeCost(self, a: int, b: int):
        """
        2点間のパスに含まれる辺のコストの和を返却する。
        O(log(2V))
        input
            a: 1点目のノード番号 (0-indexed)
            b: 2点目のノード番号 (0-indexed)
        output
            2点間の辺のコストの総和
        """
        if self.segEdgeAllSum == None:
            print("you need call edgeAllSumBuild()")
            raise Exception("segEdgeAllSum is None")
        lca = self.getLca(a, b)
        return self._getPathEdgeCostFromRoot(a) + \
            self._getPathEdgeCostFromRoot(b) - \
            self._getPathEdgeCostFromRoot(lca) * 2

    def updateVertexCost(self, x: int, cost: int):
        """
        ノードxのコストをcostに変更する。
        """
        self.vertexCosts[x] = cost

        l = self.nodeIn[x]
        r = self.nodeOut[x]

        if self.segVertexPosSum == None:
            print("you need call vertexPosSumBuild()")
            raise Exception("segVertexPosSum is None")
        self.segVertexPosSum.pointUpdate(l, cost)

        if self.segVertexAllSum == None:
            print("you need call vertexAllSumBuild()")
            raise Exception("segVertexAllSum is None")
        self.segVertexAllSum.pointUpdate(l, cost)
        self.segVertexAllSum.pointUpdate(r, -cost)

    def updateEdgeCost(self, a: int, b: int, cost: int):
        """
        辺(a -> b)のコストをcostに変更する。
        """
        print("self.G will be durty: グラフself.Gは更新されないので以降使用しないこと")

        l = self.nodeIn[b]
        r = self.nodeOut[b]
    
        if self.segEdgePosSum == None:
            print("you need call edgePosSumBuild()")
            raise Exception("segEdgePosSum is None")
        self.segEdgePosSum.pointUpdate(l, cost)

        if self.segEdgeAllSum == None:
            print("you need call edgeAllSumBuild()")
            raise Exception("segEdgeAllSum is None")
        self.segEdgeAllSum.pointUpdate(l, cost)
        self.segEdgeAllSum.pointUpdate(r, -cost)

if __name__ == "__main__":
    # グラフ
    # ■ [ノード番号](辺のコスト)    ■ <ノードのコスト>
    #            [0]                      [<1>]
    #        (2)/   \(6)                 /   \ 
    #         [1]   [5]               [<2>]   [<6>]
    #     (3)/   \(5)  \(1)           /   \     \
    #      [2]   [4]   [6]         [<3>]   [<5>]  [<1>]
    #  (4)/              \(1)       /              \
    #   [3]               [7]    [<4>]              [<1>]
    #
    N = 8
    rootNode = 0
    vertexCosts = [1, 2, 3, 4, 5, 6, 1, 1]
    er = EulerTour(N, rootNode, vertexCosts)
    Edges = [
        (0, 1, 2),
        (1, 2, 3),
        (2, 3, 4),
        (1, 4, 5),
        (0, 5, 6),
        (5, 6, 1),
        (6, 7, 1),
    ]

    for fromNode, toNode, cost in Edges:
        er.addEdge(fromNode, toNode, cost)
        er.addEdge(toNode, fromNode, cost)
    er.build()

    print("preOrder:", er.preOrder)
    print("postOrder:", er.postOrder)
                                        # Node:     0   1   2   3   4   5   6   7
    print("Parent:", er.parent)         # 親    [None,  0,  1,  2,  1,  0,  5,  6]
    print("Nodein:", er.nodeIn)         # 入Step[   0,  1,  2,  3,  6,  9, 10, 11]
    print("Nodeout:", er.nodeOut)       # 出Step[  15,  8,  5,  4,  7, 14, 13, 12]
    print("nodeDepth", er.nodeDepth)    # Depth [   0,  1,  2,  3,  2,  1,  2,  3]

                                                            # STEP:  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
    print("eulerTourPath:", er.eulerTourPath)               # Node  [0,  1,  2,  3,  2,  1,  4,  1,  0,  5,  6,  7,  6,  5,  0] END
    print("eulerTourDepth", er.eulerTourDepth)              # Depth [0,  1,  2,  3,  2,  1,  2,  1,  0,  1,  2,  3,  2,  1,  0]
    print("vertexCostsPosOnly", er.vertexCostsPosOnly)      #       [1,  2,  3,  4,  0,  0,  5,  0,  0,  6,  1,  1,  0,  0,  0,  0]     # 行きがけ時にノードコストを計上
    print("vertexCostPosAndNeg", er.vertexCostsPosAndNeg)   #       [1,  2,  3,  4, -4, -3,  5, -5, -2,  6,  1,  1, -1, -1, -6, -1]     # 行きがけ(正)/帰りがけ(負)時にノードコストを計上
    print("edgeCostPosOnly", er.edgeCostsPosOnly)           #       [0,  2,  3,  4,  0,  0,  5,  0,  0,  6,  1,  1,  0,  0,  0,  0]     # 行きがけ時に辺のコストを計上
    print("edgeCostPosAndNeg", er.edgeCostsPosAndNeg)       #       [0,  2,  3,  4, -4, -3,  5, -5, -2,  6,  1,  1, -1, -1, -6,  0]     # 行きがけ(正)/帰りがけ(負)時に辺のコストを計上

    er.lcaBuild()
    # LCA算出
    print(er.getLca(3, 4)) # 1

    er.vertexPosSumBuild()
    # ノード1を根とする部分木のノードコストの和
    print(er.getPartialTreeVertexCost(1)) # 14
    
    er.edgePosSumBuild()
    # ノード1を根とする部分木の辺のコストの和
    print(er.getPartialTreeEdgeCost(1)) # 12
    
    er.vertexAllSumBuild()
    # 根からノード3までの部分木のノードコストの和
    print(er._getPathVertexCostFromRoot(3)) # 10
    # ノード3からノード4までの部分木のノードコストの和
    print(er.getPathVertexCost(3, 4)) # 14

    er.updateVertexCost(1, 100)
    er.updateVertexCost(6, 10000)
    
    print(er.getPathVertexCost(3, 4)) # 112

    er.edgeAllSumBuild()
    # 根からノード3までの部分木の辺のコストの和
    print(er._getPathEdgeCostFromRoot(3)) # 9
    # ノード3からノード4までの部分木の辺のコストの和
    print(er.getPathEdgeCost(3, 4)) # 12
    
    # 辺のコストを更新
    er.updateEdgeCost(1, 2, 100)
    er.updateEdgeCost(5, 6, 10000)
    
    print(er.getPathEdgeCost(3, 4)) # 109