#!/usr/bin/env python3
import sys

def solve(N: int, M: int, A: "List[int]", B: "List[int]"):
    # N = 2000
    # A = [i + 1 for i in range(1990)]
    # B = [i + 2 for i in range(1990)]

    from collections import deque
    INF = 10 ** 9
    def bfs(edges: "List[to]", start_node: int) -> list:
        # deprecated
        count = 0
        q = deque()
        dist = [INF] * len(edges)
        q.append(start_node)
        dist[start_node] = 0
        while q:
            now = q.pop()
            for next in edges[now]:
                if dist[next] != INF:
                    continue
                q.append(next)
                dist[next] = dist[now] + 1
                count += 1
        return count
    field = [[] for _ in range(N)]
    
    ans = N
    for aa, bb in zip(A, B):
        field[aa - 1].append(bb - 1)
    for s in range(N):
        ans += bfs(field, s)
    print(ans)
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int()] * (M)  # type: "List[int]"
    B = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, M, A, B)

if __name__ == '__main__':
    main()
