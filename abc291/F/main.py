#!/usr/bin/env python3
import sys
INF = 10 ** 16

from collections import deque
def bfs(G: "List[to]", start_node: int) -> list:
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

def solve(N: int, M: int, S: "List[str]"):
    G = [[] for _ in range(N)]
    revG = [[] for _ in range(N)]
    for i in range(N):
        for mm in range(M):
            if S[i][mm] == "1":
                G[i].append(i + mm + 1)
                revG[i + mm + 1].append(i)

    def dis_bfs(start_node: int, ban: int) -> list:
        offset = start_node
        q = deque()
        dist = [INF] * len(G)
        q.append(start_node)
        dist[start_node - offset] = 0
        while q:
            now = q.popleft()
            for next in G[now]:
                if next == ban or dist[next - offset] != INF:
                    continue
                if next < ban:
                    q.append(next)
                dist[next - offset] = dist[now - offset] + 1
        return dist
    d1 = bfs(G, 0)
    d2 = bfs(revG, N - 1)
    # print(d1)
    # print(d2)
    ans = []
    for k in range(1, N - 1):
        pre = max(0, (k - M - 1))
        tmp = INF
        for st in range(pre, k):
            for next in G[st]:
                if next <= k:
                    continue
                tmp = min(tmp, d1[st] + d2[next] + 1)
        ans.append(-1 if tmp == INF else tmp)
    print(*ans, sep=" ")
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
