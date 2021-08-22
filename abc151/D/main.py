#!/usr/bin/env python3
import sys

def main():
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
            for via in range(self.H * self.W):
                for start in range(self.H * self.W):
                    for goal in range(self.H * self.W):
                        self.dp[start][goal] = min(self.dp[start][goal], self.dp[start][via] + self.dp[via][goal])
        
    H, W = map(int, sys.stdin.readline().split())
    G = [sys.stdin.readline() for _ in range(H)]
    wf = WarshallFloyd(H, W)
    wf.setGraph(G)
    wf.build()

    ans = 0
    for sy in range(H):
        for sx in range(W):
            if G[sy][sx] == "#":
                continue
            for gy in range(H):
                for gx in range(W):
                    if G[gy][gx] == "#":
                        continue
                    ans = max(ans, wf.dp[wf.convertNode(sy, sx)][wf.convertNode(gy, gx)])
    print(ans)

if __name__ == '__main__':
    main()
