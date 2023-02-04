#!/usr/bin/env python3
import sys
from collections import deque
sys.setrecursionlimit(10 ** 9)

def solve(N: int, X: int, Y: int, U: "List[int]", V: "List[int]"):
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        G[U[i] - 1].append(V[i] - 1)
        G[V[i] - 1].append(U[i] - 1)

    l = deque()
    def dfs(pre: int, cur: int):
        l.append(cur + 1)
        if cur == Y - 1:
            print(*l)
            return
        for next in G[cur]:
            if next == pre:
                continue
            dfs(pre=cur, cur=next)
        l.pop()
    
    dfs(pre=-1, cur=X-1)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    U = [int()] * (N - 1)  # type: "List[int]"
    V = [int()] * (N - 1)  # type: "List[int]"
    for i in range(N - 1):
        U[i] = int(next(tokens))
        V[i] = int(next(tokens))
    solve(N, X, Y, U, V)

if __name__ == '__main__':
    main()