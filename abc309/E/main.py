#!/usr/bin/env python3
import sys
INF = 10 ** 16
from collections import defaultdict
class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int, func: "function(int, int)"):
        self.initVal = initVal
        self.func = func
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    """ 一点加算
    tree[index] += val
    """
    def pointAdd(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val # Add
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
    
    """ 一点更新
    tree[index] = val
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = val # Update # 更新方法も変更が必要な場合は書き換えること。 eg.) XOR演算など |= val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])

    """ 区間最小値 (RMQ) / 区間和 (RSQ)
    """
    def rangeQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = self.initVal
        while l < r:
            if l % 2 == 1:
                res = self.func(res, self.tree[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                res = self.func(res, self.tree[r - 1])
                r -= 1
            r //= 2
        return res

needCheck = defaultdict(int)
depthCount = defaultdict(int)

def solve(N: int, M: int, p: "List[int]", x: "List[int]", y: "List[int]"):
    score = [0] * N
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

            # SegmentTree
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
            for i in range(self.N):
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

                    # ついた
                    if curNode in needCheck and needCheck[curNode] != 0:
                        target = self.nodeDepth[curNode] + needCheck[curNode]
                        # print(target)
                        depthCount[target] += 1
                        # print(depthCount)
                    
                    if self.nodeDepth[curNode] in depthCount:
                        # print(curNode, "#", depthCount[self.nodeDepth[curNode]])
                        # print(needCheck)
                        # print(depthCount)
                        score[curNode] -= depthCount[self.nodeDepth[curNode]]
                    
                    # needCheck -> ノードiは あとval世代したで-1しないといけない
                    # depthCount -> ノードiは -valしないといけない

                    # 葉である場合は帰りがけの処理もする
                    if len(self.G[curNode]) == 1:
                        self.nodeOut[curNode] = curStep + 1
                        self.postorderCount[curNode] = (curStep, curNode)

                        # かえる
                        if curNode in needCheck and needCheck[curNode] != 0:
                            target = self.nodeDepth[curNode] + needCheck[curNode]
                            # print(target)
                            depthCount[target] -= 1

                    
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

                    # かえる
                    if curNode in needCheck and needCheck[curNode] != 0:
                        target = self.nodeDepth[curNode] + needCheck[curNode]
                        # print(target)
                        depthCount[target] -= 1

                # 次のStepへ
                curStep += 1

            # 最後の調整
            self.vertexCostsPosOnly.append(0)
            self.vertexCostsPosAndNeg.append(-self.vertexCosts[self.rootNode])
            self.edgeCostsPosOnly.append(0)
            self.edgeCostsPosAndNeg.append(0)
            self.postorderCount.sort()
            self.postOrder = [nodeNum for _, nodeNum in self.postorderCount]

    er = EulerTour(N, 0)
    p = [0] + p
    for now in range(1, N):
        er.addEdge(now, p[now] - 1, 0)
        er.addEdge(p[now] - 1, now, 0)

    for xx, yy in zip(x, y):
        if xx - 1 not in needCheck:
            score[xx - 1] += 1
        needCheck[xx - 1] = max(needCheck[xx - 1], yy + 1)

    er.build()

    from collections import deque
    # print(score)
    q = deque()
    q.append(0)
    while q:
        now = q.popleft()
        for next in er.G[now]:
            next = next[0]
            if er.nodeDepth[now] > er.nodeDepth[next]:
                continue
            score[next] += score[now]
            q.append(next)
    ans = 0
    for i in score:
        if i >= 1:
            ans += 1
    print(ans)


    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    p = [int(next(tokens)) for _ in range(N - 2 + 1)]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, M, p, x, y)

if __name__ == '__main__':
    main()
