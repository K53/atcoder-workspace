#!/usr/bin/env python3
import sys
from collections import deque


com = {
    (1, 0): 0,
    (0, 1): 1,
    (-1, 0): 2,
    (0, -1): 3
}

def solve(N: int, M: int, S: "List[str]"):
    def bfs(startY, startX) -> list:
        # ゴールやスタートを任意に設定できる問題では開始点が壁であるケースに注意!!!!
        INF = 10 ** 16
        q = deque()
        dist = [[[INF] * 4 for _ in range(M)] for _ in range(N)]
        q.append((startY, startX, 1, 0)) # y方向 / x方向
        q.append((startY, startX, 0, 1)) # y方向 / x方向
        q.append((startY, startX, -1, 0)) # y方向 / x方向
        q.append((startY, startX, 0, -1)) # y方向 / x方向
        dist[startY][startX][com[(1, 0)]] = 1
        dist[startY][startX][com[(0, 1)]] = 1
        dist[startY][startX][com[(-1, 0)]] = 1
        dist[startY][startX][com[(0, -1)]] = 1
        while q:
            nowy, nowx, nowdy, nowdx = q.popleft()
            nexty = nowy + nowdy
            nextx = nowx + nowdx
            if dist[nexty][nextx][com[(nowdy, nowdx)]] != INF:
                continue
            if S[nexty][nextx] == "#":
                for nextdy, nextdx in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    if nextdy == nowdy and nextdx == nowdx:
                        continue
                    nexty_turned = nowy + nextdy
                    nextx_turned = nowx + nextdx
                    if dist[nexty_turned][nextx_turned][com[(nextdy, nextdx)]] != INF or S[nexty_turned][nextx_turned] == "#":
                        continue
                    q.append((nexty_turned, nextx_turned, nextdy, nextdx))
                    dist[nexty_turned][nextx_turned][com[(nextdy, nextdx)]] = 1
                continue
            q.append((nexty, nextx, nowdy, nowdx))
            dist[nexty][nextx][com[(nowdy, nowdx)]] = 1
        return dist

    d = bfs(1, 1)
    ans = 0
    for i in range(N):
        for j in range(M):
            for k in range(4):
                if d[i][j][k] == 1:
                    ans += 1
                    break
    # print(d)
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
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, M, S)

if __name__ == '__main__':
    main()
