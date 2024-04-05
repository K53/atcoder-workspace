#!/usr/bin/env python3
# import sys
# sys.setrecursionlimit(10 ** 9)
n = int(input())
*a, = map(int, input().split())
d = [0] * 3
for e in a:
    d[e - 1] += 1

dp = [[[-1.0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0.0

def f(c1, c2, c3):
    if dp[c1][c2][c3] != -1.0:
        return dp[c1][c2][c3]
    res = n
    if c1 > 0:
        res += f(c1 - 1, c2, c3) * c1
    if c2 > 0:
        res += f(c1 + 1, c2 - 1, c3) * c2
    if c3 > 0:
        res += f(c1, c2 + 1, c3 - 1) * c3
    res /= (c1 + c2 + c3)
    dp[c1][c2][c3] = res
    return res
    
print(f(d[0], d[1], d[2]))