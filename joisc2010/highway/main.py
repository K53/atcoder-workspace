#!/usr/bin/env python3
import sys
INF = 10 ** 16

class SegTree:
    def __init__(self, monoid: int, bottomList: "list[int]", func: "function", convertLengthToThePowerOf2: bool = False):
        self.monoid = monoid
        self.func = func
        if convertLengthToThePowerOf2:
            self.actualLen = len(bottomList)
            self.bottomLen = self.getSegLenOfThePowerOf2(len(bottomList))
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [monoid] * self.segLen
        else:
            self.actualLen = len(bottomList)
            self.bottomLen = len(bottomList)
            self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
            self.segLen = self.bottomLen * 2
            self.tree = [monoid] * self.segLen
        self._build(bottomList)

    def _build(self, seq):
        """
        初期化
        O(self.segLen)
        """
        # 最下段の初期化
        for i, x in enumerate(seq, self.offset):
            self.tree[i] = x
        # ビルド
        for i in range(self.offset - 1, 0, -1):
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1])

    def getSegLenOfThePowerOf2(self, ln: int):
        """
        直近の2べきの長さを算出
        """
        if ln <= 0:
            return 1
        else:    
            import math
            decimalPart, integerPart = math.modf(math.log2(ln))
            return 2 ** (int(integerPart) + 1)

    def pointAdd(self, i: int, val: int):
        """
        一点加算 他演算
        O(log(self.bottomLen))
        """
        i += self.offset
        self.tree[i] += val
        # self.tree[i] = self.func(self.tree[i], val) <- こっちの方が都度の修正は発生しない。再帰が遅くないか次第。
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

    def pointUpdate(self, i: int, val: int):
        """
        一点更新
        O(log(self.bottomLen))
        """
        i += self.offset
        self.tree[i] = val
        while i > 1:
            i >>= 1 # 2で割って頂点に達するまで下層から遡上
            self.tree[i] = self.func(self.tree[i << 1], self.tree[i << 1 | 1]) # 必ず末尾0と1がペアになるのでor演算子

    def getRange(self, l: int, r: int):
        """
        区間取得 (l ≦ X < r)
        l ~ r-1までの区間 (0-indexed)。※右端を含まない。
        O(log(self.bottomLen))
        """
        l += self.offset
        r += self.offset
        vL = self.monoid
        vR = self.monoid
        while l < r:
            if l & 1:
                vL = self.func(vL, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                vR = self.func(self.tree[r], vR)
            l >>= 1
            r >>= 1
        return self.func(vL, vR)

    def getPoint(self, i: int):
        """
        一点取得
        O(1)
        """
        i += self.offset
        return self.tree[i]

    def max_right(self, l, is_ok: "function"):
        """
        二分探索
        O(log(self.bottomLen))
        ※ セグ木上の二分探索をする場合は2べきにすること。
        # !!!! ng側が返却される !!!!!
        """
        print("セグ木上の二分探索をする場合は2べきにすること。")
        l += self.offset
        ll = l // (l & -l) # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
        ans = self.monoid
        while is_ok(self.func(ans, self.tree[ll])): # そのセグメントが条件を満たすかどうかの判定
            ans = self.func(ans, self.tree[ll])
            ll += 1
            while ~ll & 1: # llの反転 ~ll = -(ll+1)
                ll >>= 1 # lから始まる含む最も大きいセグメントのインデックス算出。(= 2で割れなくなるまで割る)
            if ll == 1: # 最上層まで到達したら全範囲満たすということ。 → (2べきになるようにモノイド埋めする前の)実際の長さを返す。
                return self.actualLen
        while ll < self.offset:
            ll <<= 1 # 一階層下のセグメントへ移動 (=2倍)
            if is_ok(self.func(ans, self.tree[ll])): # 条件を満たすなら同一階層の隣のセグメントの下層へ。満たさないならそのまま下層へ。
                ans = self.func(ans, self.tree[ll])
                ll += 1
        return ll - self.offset # ng側が返る

    # 未検証
    def min_left(self, r, is_ok):
        r += self.offset
        rr = max(r // (~r & -~r), 1)
        ans = self.monoid
        while is_ok(self.func(self.tree[rr], ans)):
            ans = self.func(self.tree[rr], ans)
            rr -= 1
            while rr & 1:
                rr >>= 1
            if rr == 0:
                return -1
        while rr < self.offset:
            rr <<= 1
            if is_ok(self.func(self.tree[rr+1], ans)):
                ans = self.func(self.tree[rr+1], ans)
            else:
                rr += 1
        return rr - self.offset

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
        
        # self.usedPreorder = [False] * self.N
        # self.preorder = []
        # self.postordercnt = [-1] * self.N
        # self.postorder = []

        # SegTree
        self.segLca = None # LCA用
        self.segVertexPosSum = None # 部分木用(ノード)
        self.segEdgePosSum = None # 部分木用(辺)
        self.segVertexAllSum = None # パスクエリ用(ノード)
        self.segEdgeAllSum = None # パスクエリ用(辺)

    # 辺の追加
    def addEdge(self, fromNode: int, toNode: int, cost: int):
        self.G[fromNode].append((toNode, cost))
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
                self.eulerTourDepth.append(curdepth)
                self.eulerTourPath.append(curNode)
                self.edgeCostsPosOnly.append(vcost)
                self.edgeCostsPosAndNeg.append(vcost)
                self.vertexCostsPosOnly.append(ecost)
                self.vertexCostsPosAndNeg.append(ecost)

                # 葉である場合は帰りがけの処理もする
                if len(self.G[curNode]) == 1:
                    self.nodeOut[curNode] = curStep + 1
                
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
                self.eulerTourPath.append(curNode)
                self.edgeCostsPosOnly.append(0)
                self.edgeCostsPosAndNeg.append(-vcost)
                self.vertexCostsPosOnly.append(0)
                self.vertexCostsPosAndNeg.append(ecost)
                self.eulerTourDepth.append(curdepth)
                self.nodeOut[curNode] = curStep + 1

            # 次のStepへ
            curStep += 1

        # 最後の調整
        self.vertexCostsPosOnly.append(0)
        self.vertexCostsPosAndNeg.append(-self.vertexCosts[self.rootNode])
        self.edgeCostsPosOnly.append(0)
        self.edgeCostsPosAndNeg.append(0)

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

    def _pathQueryVertexCostFromRoot(self, x: int):
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

    def _pathQueryEdgeCostFromRoot(self, x: int):
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

    def pathQueryVertexCost(self, a: int, b: int):
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
        return self._pathQueryVertexCostFromRoot(a) + \
            self._pathQueryVertexCostFromRoot(b) - \
            self._pathQueryVertexCostFromRoot(lca) * 2 + \
            self.vertexCosts[lca]

    def pathQueryEdgeCost(self, a: int, b: int):
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
        return self._pathQueryEdgeCostFromRoot(a) + \
            self._pathQueryEdgeCostFromRoot(b) - \
            self._pathQueryEdgeCostFromRoot(lca) * 2

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
    N, M = map(int, input().split())
    er = EulerTour(N, 0, [0] * N)
    loads = []
    for _ in range(N - 1):
        f, t = map(int, input().split())
        loads.append((f - 1, t - 1))
        er.addEdge(f - 1, t - 1, 1)
        er.addEdge(t - 1, f - 1, 1)
    er.build()
    er.lcaBuild()
    er.edgePosSumBuild()
    er.edgeAllSumBuild()
    for _ in range(M):
        type, *query = map(str, input().split())
        if type == "I":
            l, up, down = map(int, query)
            f, t = loads[l - 1]
            # f=>t : up
            # f<=t : down
            if f < t:
                er.updateEdgeCost(f, t, up)
                er.updateEdgeCost(t, f, down)
            else:
                er.updateEdgeCost(t, f, up)
                er.updateEdgeCost(f, t, down)
        else:
                                                                        # STEP:  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
            print("eulerTourPath:", er.eulerTourPath)               # Node  [0,  1,  2,  3,  2,  1,  4,  1,  0,  5,  6,  7,  6,  5,  0] END
            print("eulerTourDepth", er.eulerTourDepth)              # Depth [0,  1,  2,  3,  2,  1,  2,  1,  0,  1,  2,  3,  2,  1,  0]
            print("edgeCostPosOnly", er.edgeCostsPosOnly)           #       [0,  2,  3,  4,  0,  0,  5,  0,  0,  6,  1,  1,  0,  0,  0,  0]     # 行きがけ時に辺のコストを計上
            print("edgeCostPosAndNeg", er.edgeCostsPosAndNeg)       #       [0,  2,  3,  4, -4, -3,  5, -5, -2,  6,  1,  1, -1, -1, -6,  0]     # 行きがけ(正)/帰りがけ(負)時に辺のコストを計上

            x, y = map(int, query)
            print(er.pathQueryEdgeCost(x - 1, y - 1))
            exit()


# eulerTourPath:        [0, 2, 3, 2, 1, 2, 0]
# eulerTourDepth        [0, 1, 2, 1, 2, 1, 0]
# edgeCostPosOnly       [0, 1, 1, 0, 1, 0, 0, 0]
# edgeCostPosAndNeg     [0, 1, 1, -1, 1, -1, -1, 0]