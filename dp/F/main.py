#!/usr/bin/env python3
import sys

def main():
    s = input()
    t = input()
    dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
    for i in range(len(t)):
        for j in range(len(s)):
            if t[i] == s[j]:
                dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j + 1])
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j+ 1])

    # for i in range(len(t) + 1):
    #     print(dp[i])
    from collections import deque
    def bfs(dp, H, W, startY, startX) -> list:
        INF = 10 ** 16
        q = deque()
        dist = [[INF] * W for _ in range(H)]
        q.append((startY, startX))
        dist[startY][startX] = 0
        ans = []
        while q:
            nowy, nowx = q.popleft()
            upy, upx = nowy - 1, nowx
            lefty, leftx = nowy, nowx - 1

            if upy < 0 or upx < 0 or upy >= H or upx >= W or dist[upy][upx] != INF:
                continue
            
            if lefty < 0 or leftx < 0 or lefty >= H or leftx >= W or dist[lefty][leftx] != INF:
                continue
            
            if dp[upy][upx] != dp[nowy][nowx] and dp[lefty][leftx] != dp[nowy][nowx]:
                q.append((nowy - 1, nowx - 1))
                ans.append(t[nowy - 1])
            elif dp[upy][upx] == dp[nowy][nowx]:
                q.append((upy, upx))
            elif dp[lefty][leftx] == dp[nowy][nowx]:
                q.append((lefty, leftx))

        return ans
    
    res = bfs(dp, len(t) + 1, len(s) + 1, len(t), len(s))
    print(*res[::-1], sep="")
    return

if __name__ == '__main__':
    main()
