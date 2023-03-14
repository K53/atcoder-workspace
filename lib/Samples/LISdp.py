# ------------------------------------------------------------------------------
#     LIS (最長増加部分列)
# ------------------------------------------------------------------------------
#
# Order
#   O(NlogN)
# 参考
#  - https://tjkendev.github.io/procon-library/python/dp/lis.html
#  - https://qiita.com/python_walker/items/d1e2be789f6e7a0851e5
# verify
#  - https://atcoder.jp/contests/abc006/tasks/abc006_4
# ------------------------------------------------------------------------------
import bisect
INF = 10 ** 16

L = [1, 3, 5, 2, 4, 6]
N = len(L)

# dp[i] := 長さiとなる最長部分増加列(LIS)の中で列の最後の要素の最小値
dp = [INF] * (N + 1)
dp[0] = -1 # Lのどの要素よりも小さい値を初期値にする。
for ll in L:
    idx = bisect.bisect_right(dp, ll - 1) # dp[idx]までは再利用し、末尾をccに書き換える。
    dp[idx] = min(dp[idx], ll)

ans = 0
for i in range(N + 1):
    if dp[i] == INF:
        continue
    ans = max(ans, i)

# 最長の増加列の長さ
print(ans)