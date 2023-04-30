#!/usr/bin/env python3

N, Q = map(int, input().split())
c = list(map(int, input().split()))

total_kinds = 0
each_count = [0] * (max(c) + 1)
queries = []
for i in range(Q):
    l, r = map(int, input().split())
    queries.append([l - 1, r, i])

sq = int(Q ** 0.5)
unit = max(c) // sq + 1
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

# areaの偶奇で交互になるように配置
mo_list = []
for i in range(len(sqrt_divideds)):
    if i & 1:
        mo_list += sorted(sqrt_divideds[i], key=lambda x: x[1])[::-1]
        continue
    mo_list += sorted(sqrt_divideds[i], key=lambda x: x[1])

def _add(k):
    global total_kinds
    if each_count[k] == 0:
        total_kinds += 1
    each_count[k] += 1

def _del(k):
    global total_kinds
    each_count[k] -= 1
    if each_count[k] == 0:
        total_kinds -= 1
 
ans = [-1] * Q
cur_l, cur_r = 0, 0
for i in range(Q):
    ll, rr, idx = mo_list[i]
    # print(i, "---", cur_l, ll, cur_r, rr)
    while cur_l > ll:
        cur_l -= 1
        _add(c[cur_l]) # 移動先を足す
    while cur_l < ll:
        _del(c[cur_l]) # 移動元を引く
        cur_l += 1
    while cur_r > rr:
        cur_r -= 1
        _del(c[cur_r]) # 移動先を引く
    while cur_r < rr:
        _add(c[cur_r]) # 移動元を足す
        cur_r += 1
    ans[idx] = total_kinds
print(*ans, sep="\n")

