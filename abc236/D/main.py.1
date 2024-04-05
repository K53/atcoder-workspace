#!/usr/bin/env python3
ans = 0
N = int(input())
A = [[0] * 2 * N for _ in range(2 * N)]
used = [False] * 2 * N
for i in range(2 * N - 1):
    l = list(map(int, input().split()))
    for j in range(len(l)):
        A[i][i + j + 1] = l[j]
        A[i + j + 1][i] = l[j]

def dfs(l):
    global ans
    if len(l) == N:
        # print(l)
        tmp = 0
        for i, j in l:
            tmp ^= A[i][j]
        ans = max(ans, tmp)
    else:
        mi = min(i for i in range(2 * N) if not used[i])
        used[mi] = True
        for j in range(mi + 1, 2 * N):
            if used[j]:
                continue
            used[j] = True
            dfs(l + [(mi, j)])
            used[j] = False
        used[mi] = False
dfs([])
print(ans)

