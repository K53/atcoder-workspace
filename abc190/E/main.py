#!/usr/bin/env python3
import sys
from collections import deque
def solve():
    N, M = map(int, input().split())
    G = [[] * N for _ in range(N)]
    for _ in range(M):
        a,b = map(lambda x: int(x) - 1, input().split())
        G[a].append(b)
        G[b].append(a)
        
    K = int(input())
    C = list(map(lambda x: int(x) - 1, input().split()))
    
    INF = 10 ** 16
    def bfs(start_node: int) -> list:
        q = deque()
        dist = [INF] * len(G)
        q.append(start_node)
        dist[start_node] = 0
        while q:
            now = q.popleft()
            for next in G[now]:
                if dist[next] != INF:
                    continue
                q.append(next)
                dist[next] = dist[now] + 1
        return dist

    memo = [[0] * K for _ in range(K)]
    for s in range(K):
        d = bfs(C[s])
        for g in range(K):
            memo[s][g] = d[C[g]]
            memo[g][s] = d[C[g]]
            

    dp = [[INF] * K for _ in range(2 ** K)]
    for i in range(K):
        dp[2 ** i][i] = 1

    for i in range(2 ** K):
        for cur in range(K):
            if (i >> cur) & 1:
                for next in range(K):
                    if memo[cur][next] == INF:
                        continue
                    dp[i | (2 ** next)][next] = min(dp[i | (2 ** next)][next], dp[i][cur] + memo[cur][next])
            
    ans = min(dp[-1])
    print(ans if ans != INF else -1)

if __name__ == '__main__':
    solve()