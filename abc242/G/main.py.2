#!/usr/bin/env python3
import sys
from functools import cmp_to_key
input = lambda: sys.stdin.readline().strip()
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
queries = []
for i in range(Q):
    l, r = map(int, input().split())
    queries.append((l - 1, r, i))


# Mo's Algorithm =============
sq = Q ** 0.5
# aがbよりも前に置くなら-1、後ろに置くなら1
@cmp_to_key
def _f(a, b):
    if a[0]//sq != b[0]//sq:
        if a[0] > b[0]: return 1
        if a[0] < b[0]: return -1
        return 0
    else:
        if a[0]//sq % 2 == 0:
            if a[1] > b[1]: return 1
            if a[1] < b[1]: return -1
            return 0
        else:
            if a[1] > b[1]: return -1
            if a[1] < b[1]: return 1
            return 0
    
lr = sorted(queries, key=_f)
# print(lr)
total_pairs = 0
each_count = [0] * (N + 1)

ans = [-1] * Q
cur_l, cur_r = 0, 0
for i in range(Q):
    ll, rr, idx = lr[i]
    # print(i, "---", cur_l, ll, cur_r, rr, ":", total_pairs, each_count)
    while cur_l > ll:
        cur_l -= 1
        each_count[A[cur_l]] += 1
        if each_count[A[cur_l]] % 2 == 0:
            total_pairs += 1
    while cur_l < ll:
        if each_count[A[cur_l]] % 2 == 0:
            total_pairs -= 1
        each_count[A[cur_l]] -= 1
        cur_l += 1
    while cur_r > rr:
        cur_r -= 1
        if each_count[A[cur_r]] % 2 == 0:
            total_pairs -= 1
        each_count[A[cur_r]] -= 1
    while cur_r < rr:
        # print("", total_pairs, each_count)
        each_count[A[cur_r]] += 1
        if each_count[A[cur_r]] % 2 == 0:
            total_pairs += 1
        cur_r += 1
    ans[idx] = total_pairs
print(*ans, sep="\n")

