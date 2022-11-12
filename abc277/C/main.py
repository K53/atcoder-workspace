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

def solve(N: int, A: "List[int]", B: "List[int]"):
    compressed = {}
    compressed_to_raw = []
    for index, val in enumerate(sorted(list(set(A + [1]) | set(B)))):
        compressed[val] = index
        compressed_to_raw.append(val)
    # print(compressed)
    G = [[] for _ in range(len(compressed))]
    for i in range(N):
        # print(i)
        G[compressed[A[i]]].append(compressed[B[i]])
        G[compressed[B[i]]].append(compressed[A[i]])

    # print(G)
    # print(compressed[1])
    d = bfs(G=G, start_node=compressed[1])
    # print(d)
    for i in reversed(range(len(d))):
        if d[i] != INF:
            print(compressed_to_raw[i])
            return


    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
