# = ワーシャルフロイド(グラフ) =======================================================================
INF = 10 ** 16
class WarshallFloyd():
    def __init__(self, N):
        self.N = N
        dp = [[INF] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0
        self.dp = dp
    
    # 自己ループを持つグラフの扱いは注意。
    def addEdge(self, fromNode: int, toNode: int, cost: int = 1):
        self.dp[fromNode][toNode] = cost
    
    def build(self):
        """
        0 〜 (via - 1)までの地点だけを利用して求めたdpテーブルを使い、viaを経由地とした時の更新処理している。
        """
        for via in range(self.N):
            for start in range(self.N):
                for goal in range(self.N):
                    if self.dp[start][via] == INF or self.dp[via][goal] == INF:
                        continue
                    # print(via, start, goal, ":", self.dp[start][goal], "<", self.dp[start][via], "+", self.dp[via][goal])
                    self.dp[start][goal] = min(self.dp[start][goal], self.dp[start][via] + self.dp[via][goal])
                    # print_for_inf_replacable(self.dp, INF)
        return self.dp
    

        # これも同じことである。
        # start - goal間を固定して、全てのviaを見た中で番距離が小さいものmin_distをとって
        # dp[start][goal]をmin_distで更新する。
        #
        # for start in range(self.N):
        #     for goal in range(self.N): # 双方向の二重カウントを防ぐなら range(start + 1, N)
        #         min_dist =  INF # start - goal間の最短経路
        #         for via in range(self.N):
        #             min_dist = min(min_dist, self.dp[start][via] + self.dp[via][goal])
        #         self.dp[start][goal] = min_dist
        # return self.dp
        # https://kakedashi-engineer.appspot.com/2020/04/22/abc074d/

from Debug import print_for_inf_replacable
# N = 8
# A = [0, 0, 1, 6, 6, 7, 2, 5, 5]
# B = [1, 2, 6, 4, 7, 3, 5, 4, 3]
# C = [1, 4, 6, 2, 5, 2, 5, 1, 3]
# #
# # [0] -- [1] -- [6] -- [7]
# #  |             |      |
# # [2] -- [5] -- [4]     |
# #         |             |
# #        [3] -----------|
# #
# N = 4
# A = [0, 1, 2, 3]
# B = [1, 2, 3, 0]
# C = [2, 4, 1, 2]
N = 6
A = [0, 0, 1, 1, 4, 3, 2]
B = [1, 2, 3, 4, 3, 5, 5]
C = [3, 10, 8, 4, 1, 5, 4]
wf = WarshallFloyd(N)
for aa, bb, cc in zip(A, B, C):
    wf.addEdge(aa, bb, cc)
    wf.addEdge(bb, aa, cc)
d = wf.build()
print_for_inf_replacable(d, replace_target=INF)



# = ワーシャルフロイド(グリッド) =======================================================================
class WarshallFloyd():
    def __init__(self, H, W):
        INF = 10 ** 16
        self.H = H
        self.W = W
        dp = [[INF] * (H * W) for _ in range(H * W)]
        for i in range(H * W):
            dp[i][i] = 0
        self.dp = dp
    
    def convertNode(self, y, x):
        return y * self.W + x
    
    def setGraph(self, grid:"List[List[int]]"):
        for y in range(self.H):
            for x in range(self.W):
                if grid[y][x] == "#":
                    continue
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nexty = y + dy
                    nextx = x + dx
                    if nexty < 0 or nextx < 0 or nexty >= self.H or nextx >= self.W or grid[nexty][nextx] == "#":
                        continue
                    self.dp[self.convertNode(y, x)][self.convertNode(nexty, nextx)] = 1

    def build(self):
        # 経由地via以下を利用してstartからgoalに辿り着く最短経路をDPする。
        for via in range(self.H * self.W):
            for start in range(self.H * self.W):
                for goal in range(self.H * self.W):
                    if self.dp[start][via] == INF or self.dp[via][goal] == INF:
                        continue
                    self.dp[start][goal] = min(self.dp[start][goal], self.dp[start][via] + self.dp[via][goal])