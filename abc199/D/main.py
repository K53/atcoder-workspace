#!/usr/bin/env python3
import copy

# 0 R
# 1 G
# 2 B

def main():
    N, M = map(int, input().split())
    edges = [[] for _ in range(M)]
    for _ in range(M):
        A, B = map(lambda i: int(i) - 1, input().split())
        edges[A].append(B)
        edges[B].append(A)
    
    def dfs(color: "list", now: int):
        res = 0
        count = len(edges[now])
        for next in edges[now]:
            print("now", now)
            print("next", next)
            print("c1", color)
            if color[next] == color[now]:
                continue
            elif color[next] == -1:
                r = 0
                for c in range(3):
                    if color[now] == c:
                        continue
                    color[next] = c
                    r += dfs(copy.copy(color), next)
                res += r
            else:
                count -= 1
                if count == 0:
                    res += 1 
            print("res", res)
        return res
     
    print(dfs([0] + [-1] * (N - 1), 0))



    


if __name__ == '__main__':
    main()
