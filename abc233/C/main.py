#!/usr/bin/env python3

ans = 0
def main():
    N, X = map(int, input().split())
    A = []
    for i in range(N):
        L, *a = map(int, input().split())
        A.append(a)
    
    def dfs(depth, prd):
        global ans
        if depth == N:
            if prd == X:
                ans += 1
            return
        for aa in A[depth]:
            dfs(depth + 1, prd * aa)

    dfs(0, 1)
    print(ans)

if __name__ == '__main__':
    main()
