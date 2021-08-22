#!/usr/bin/env python3
import sys

def main():
    INF = 10 ** 16
    class WarshallFloyd():
        def __init__(self, N):
            self.N = N
            dp = [[INF] * N for _ in range(N)]
            for i in range(N):
                dp[i][i] = 0
            self.dp = dp
        
        def addEdge(self, fromNode: int, toNode: int, cost: int = 1):
            self.dp[fromNode][toNode] = cost
        
        def build(self):
            for via in range(self.N):
                for start in range(self.N):
                    for goal in range(self.N):
                        self.dp[start][goal] = min(self.dp[start][goal], self.dp[start][via] + self.dp[via][goal])
            return self.dp

    N, M = map(int, sys.stdin.readline().split())
    wf = WarshallFloyd(N)
    for _ in range(M):
        a, b, t = map(int, sys.stdin.readline().split())
        wf.addEdge(a - 1, b - 1, t)
        wf.addEdge(b - 1, a - 1, t)
    d = wf.build()
    ans = INF
    for start in range(N):
        ans = min(ans, max(d[start]))
    print(ans)

        
if __name__ == '__main__':
    main()
