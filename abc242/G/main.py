#!/usr/bin/env python3
# from functools import cmp_to_key
import sys
input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))
Q = int(input())

total_kinds = 0
each_count = [0] * (max(A) + 1)
queries = []
for i in range(Q):
    l, r = map(int, input().split())
    queries.append([l - 1, r, i])

sq = int(Q ** 0.5)
unit = N // sq + 1
# 
# |       |       |      |           |
# | area1 | area2 |      |  area(sq) |
# |       |       |      |           |
# +----------------- ... ---------------
#  <-unit-> 
# 
sqrt_divideds = [[] for _ in range(sq + 1)]
for x, y, i in queries:
    sqrt_divideds[x // unit].append([x, y, i])

mo_list = []
for i in range(len(sqrt_divideds)):
    if i & 1:
        mo_list += sorted(sqrt_divideds[i], key=lambda x: x[1])[::-1]
        continue
    mo_list += sorted(sqrt_divideds[i], key=lambda x: x[1])
    
ans = [-1] * Q
cur_l, cur_r = 0, 0
for i in range(Q):
    ll, rr, idx = mo_list[i]
    # print(i, "---", cur_l, ll, cur_r, rr)
    while cur_l > ll:
        cur_l -= 1
        if each_count[A[cur_l]] % 2 != 0:
            total_kinds += 1
        each_count[A[cur_l]] += 1
    while cur_l < ll:
        each_count[A[cur_l]] -= 1
        if each_count[A[cur_l]] % 2 != 0:
            total_kinds -= 1
        cur_l += 1
    while cur_r > rr:
        cur_r -= 1
        each_count[A[cur_r]] -= 1
        if each_count[A[cur_r]] % 2 != 0:
            total_kinds -= 1
    while cur_r < rr:
        if each_count[A[cur_r]] % 2 != 0:
            total_kinds += 1
        each_count[A[cur_r]] += 1
        cur_r += 1
    ans[idx] = total_kinds
print(*ans, sep="\n")
