#!/usr/bin/env python3
import sys



def solve(N: int, A: "List[int]", B: "List[int]"):
    from collections import deque
    def bfs(edges: "List[to]", start_node: int) -> list:
        INF = 10 ** 16
        q = deque()
        dist = [INF] * len(edges)
        q.append(start_node)
        dist[start_node] = 0
        while q:
            now = q.popleft()
            for next in edges[now]:
                if dist[next] != INF:
                    continue
                q.append(next)
                dist[next] = 1 if dist[now] == 0 else 0
        return dist
    tree = [[] for _ in range(N)]
    for i in range(N - 1):
        tree[A[i] - 1].append(B[i] - 1)
        tree[B[i] - 1].append(A[i] - 1)
    
    d = bfs(tree, A[0])
    a = 1 if sum(d) >= (N // 2) else 0
    ans = [i + 1 for i, x in enumerate(d) if x == a]
    print(*ans[:(N // 2)], sep=" ")
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int()] * (N - 1)  # type: "List[int]"
    B = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, A, B)

if __name__ == '__main__':
    main()
