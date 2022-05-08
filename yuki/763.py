#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10 ** 9)

def main():
    N = int(input())
    G = [[] for _ in range(N)]
    dp = [0] * N
    for _ in range(N - 1):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    
    def dfs(now: int, pre: int):
        selectable = True
        for next in G[now]:
            if next == pre:
                continue
            dfs(next, now)
            if dp[next]:
                selectable = False
        if selectable:
            dp[now] = 1
        return

    dfs(0, -1)
    print(sum(dp))
    return

if __name__ == '__main__':
    main()