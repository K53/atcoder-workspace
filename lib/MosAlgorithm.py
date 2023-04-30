# ------------------------------------------------------------------------------
#     Mo's Algorithm (Moアルゴリズム)
# ------------------------------------------------------------------------------
# 解説
#  更新クエリがなく、クエリを先読みして任意の順に回答しても結果に違いを生まない問題に適応できる。
# 
#  - https://kanpurin.hatenablog.com/entry/2021/04/09/001439
#  - https://ei1333.hateblo.jp/entry/2017/09/11/211011
#
# 計算量
#  - O(N√Q + QlogQ)  : クエリのソートと平方分割したクエリ√Q
#
# verify
#  - https://atcoder.jp/contests/abc293/tasks/abc293_g
#  - https://atcoder.jp/contests/abc174/tasks/abc174_f (※ 本質的にはこれもMoで解けるが制約的にTLE)
# ------------------------------------------------------------------------------
A = [2, 5, 6, 5, 2, 1, 7, 9, 7, 2]
N = len(A)
Q = 10
input_queries = [
    (5, 5),
    (2, 4),
    (6, 7),
    (2, 2),
    (7, 8),
    (7, 9),
    (1, 8),
    (6, 9),
    (8, 10),
    (6, 8)
]

total_kinds = 0
each_count = [0] * (max(A) + 1)
queries = []
for i in range(Q):
    l, r = input_queries[i]
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
        _add(A[cur_l]) # 移動先を足す
    while cur_l < ll:
        _del(A[cur_l]) # 移動元を引く
        cur_l += 1
    while cur_r > rr:
        cur_r -= 1
        _del(A[cur_r]) # 移動先を引く
    while cur_r < rr:
        _add(A[cur_r]) # 移動元を足す
        cur_r += 1
    ans[idx] = total_kinds
print(*ans, sep="\n")









# 以下は遅い   OLD
# -------------------------------------------------------

# from functools import cmp_to_key

# def main():
#     A = [2, 5, 6, 5, 2, 1, 7, 9, 7, 2]
#     Q = 10
#     queries = [
#         (5, 5),
#         (2, 4),
#         (6, 7),
#         (2, 2),
#         (7, 8),
#         (7, 9),
#         (1, 8),
#         (6, 9),
#         (8, 10),
#         (6, 8)
#     ]

#     #---
#     sq = Q ** 0.5
#     total_kinds = 0
#     each_count = [0] * (max(A) + 1)

#     # aがbよりも前に置くなら-1、後ろに置くなら1
#     @cmp_to_key
#     def _f(a, b):
#         if a[0]//sq != b[0]//sq:
#             if a[0] > b[0]: return 1
#             if a[0] < b[0]: return -1
#             return 0
#         else:
#             if a[0]//sq % 2 == 0:
#                 if a[1] > b[1]: return 1
#                 if a[1] < b[1]: return -1
#                 return 0
#             else:
#                 if a[1] > b[1]: return -1
#                 if a[1] < b[1]: return 1
#                 return 0
        
#     lr = sorted([(queries[i][0] - 1, queries[i][1], i) for i in range(Q)], key=_f)
#     # print(lr)
#     def _add(k):
#         nonlocal total_kinds
#         if each_count[k] == 0:
#             total_kinds += 1
#         each_count[k] += 1
    
#     def _del(k):
#         nonlocal total_kinds
#         each_count[k] -= 1
#         if each_count[k] == 0:
#             total_kinds -= 1
 
#     ans = [-1] * Q
#     cur_l, cur_r = 0, 0
#     for i in range(Q):
#         ll, rr, idx = lr[i]
#         # print(i, "---", cur_l, ll, cur_r, rr)
#         while cur_l > ll:
#             cur_l -= 1
#             _add(A[cur_l]) # 移動先を足す
#         while cur_l < ll:
#             _del(A[cur_l]) # 移動元を引く
#             cur_l += 1
#         while cur_r > rr:
#             cur_r -= 1
#             _del(A[cur_r]) # 移動先を引く
#         while cur_r < rr:
#             _add(A[cur_r]) # 移動元を足す
#             cur_r += 1
#         ans[idx] = total_kinds
#     print(*ans, sep="\n")

# if __name__ == '__main__':
#     main()
