#!/usr/bin/env python3
import sys

def solve(N: int, S: "List[str]"):
    players = []
    for yy in range(N):
        for xx in range(N):
            if S[yy][xx] == "P":
                players.append(yy)
                players.append(xx)
    from collections import deque
    INF = 10 ** 16
    N3 = N ** 3
    N2 = N ** 2

    nowp1y, nowp1x, nowp2y, nowp2x = players
    q = deque()
    dist = [INF] * N ** 4
    q.append((nowp1y, nowp1x, nowp2y, nowp2x))
    dist[nowp1y * N3 + nowp1x * N2 + nowp2y * N + nowp2x] = 0
    dist[nowp2y * N3 + nowp2x * N2 + nowp1y * N + nowp1x] = 0
    while q:
        nowp1y, nowp1x, nowp2y, nowp2x = q.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nextp1y = nowp1y + dy
            nextp1x = nowp1x + dx
            nextp2y = nowp2y + dy
            nextp2x = nowp2x + dx
            if not (0 <= nextp1x < N and 0 <= nextp1y < N and S[nextp1y][nextp1x] != "#"):
                nextp1y = nowp1y
                nextp1x = nowp1x
            if not (0 <= nextp2x < N and 0 <= nextp2y < N and S[nextp2y][nextp2x] != "#"):
                nextp2y = nowp2y
                nextp2x = nowp2x
            nextNode = nextp1y * N3 + nextp1x * N2 + nextp2y * N + nextp2x
            nextNode2 = nextp2y * N3 + nextp2x * N2 + nextp1y * N + nextp1x
            curNode = nowp1y * N3 + nowp1x * N2 + nowp2y * N + nowp2x
            if dist[nextNode] == INF:
                dist[nextNode] = dist[curNode] + 1
                dist[nextNode2] = dist[curNode] + 1
                if not (nextp1y == nextp2y and nextp1x == nextp2x):
                    q.append((nextp1y, nextp1x, nextp2y, nextp2x))
                
    ans = INF
    for i in range(N):
        for j in range(N):
            ans = min(ans, dist[i * N3 + j * N2 + i * N + j])
    print(ans if ans != INF else -1)
    return


# Generated by 2.13.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()