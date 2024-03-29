#!/usr/bin/env python3
import sys


def solve(N: int, u: "List[int]", v: "List[int]"):
    sys.setrecursionlimit(10 ** 9)
    partTreeSize = [1] * N
    ans = [0] * N
    class DFS():
        def __init__(self, N: int) -> None:
            self.nodes = N                          # 頂点数
            self.G = [[] for _ in range(N)]         # グラフ
            self.seen = [False] * N                 # 各ノードが訪問済みかどうかのフラグ
            # self.firstOrder = []                    # ノードの行きがけ順(0-index)
            # self.lastOrder = []                     # ノードの帰りがけ順(0-index)

        # 辺の追加
        def addEdge(self, fromNode: int, toNode: int, cost: int, bothDirection: bool):
            self.G[fromNode].append((toNode, cost))
            if bothDirection:
                self.G[toNode].append((fromNode, cost))
        # DFS
        def build(self, now: int, depth:int):
            # ----- ノードに到着した時の処理
            ans[0] += depth
            # self.firstOrder.append(now)
            self.seen[now] = True
            # ----- 隣接する各ノードへの移動処理
            for next in self.G[now]:
                if self.seen[next[0]]:
                    continue
                # -- 隣接ノードに行く時
                # -- 移動処理 --
                self.build(next[0], depth + 1)
                # -- 隣接ノードから戻ってきた時
                partTreeSize[now] += partTreeSize[next[0]]
            # ----- ノードから戻る時の処理
            # self.lastOrder.append(now)
            return

        def build2(self, now: int):
            nonlocal ans
            # ----- ノードに到着した時の処理
            # self.firstOrder.append(now)
            self.seen[now] = True
            # ----- 隣接する各ノードへの移動処理
            for next in self.G[now]:
                if self.seen[next[0]]:
                    continue
                # -- 隣接ノードに行く時
                ans[next[0]] = ans[now] - partTreeSize[next[0]] + (N - partTreeSize[next[0]])
                # -- 移動処理 --
                self.build2(next[0])
                # -- 隣接ノードから戻ってきた時
                
            # ----- ノードから戻る時の処理
            # self.lastOrder.append(now)
            return


    d = DFS(N)
    for uu, vv in zip(u, v):
        d.addEdge(uu - 1, vv - 1, 1, bothDirection=True)
    d.build(0, 0)
    d.seen = [False] * N    
    d.build2(0)
    print(*ans, sep="\n")

    return


# Generated by 2.8.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    u = [int()] * (N - 1)  # type: "List[int]"
    v = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    solve(N, u, v)

if __name__ == '__main__':
    main()
