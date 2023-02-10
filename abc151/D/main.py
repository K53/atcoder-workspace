#!/usr/bin/env python3
INF = 10 ** 16
class WarshallFloyd():
    def __init__(self, G, H, W):
        self.G = G
        self.H = H
        self.W = W
        self.dist = [[INF] * (H * W) for _ in range(H * W)] # dist[from][to] := fromからtoへの最短経路
        for i in range(H * W):
            self.dist[i][i] = 0
        self._initDpTable()
    
    # グリッドを1次元配列で扱う
    def _convertNode(self, y, x):
        return y * self.W + x
    
    def _initDpTable(self):
        """
        distテーブルの初期化。初めからfrom→toへ移動可能な(=辺がある)場合は、dist[from][to]に1を入れる。
        """
        for y in range(self.H):
            for x in range(self.W):
                if self.G[y][x] == "#":
                    continue
                for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    nexty = y + dy
                    nextx = x + dx
                    if nexty < 0 or nextx < 0 or nexty >= self.H or nextx >= self.W or self.G[nexty][nextx] == "#":
                        continue
                    self.dist[self._convertNode(y, x)][self._convertNode(nexty, nextx)] = 1

    def build(self):
        # 経由地via以下を利用してstartからgoalに辿り着く最短経路をDPする。
        for via in range(self.H * self.W):
            for start in range(self.H * self.W):
                for goal in range(self.H * self.W):
                    self.dist[start][goal] = min(self.dist[start][goal], self.dist[start][via] + self.dist[via][goal])
        return self.dist

def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    wf = WarshallFloyd(G, H, W)
    d = wf.build()
    # print(d)
    ans = 0
    for dd in d:
        for ddd in dd:
            if ddd == INF:
                continue
            ans = max(ans, ddd)
    print(ans)
    return

        

if __name__ == '__main__':
    main()
