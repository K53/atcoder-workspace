# 最長共通部分列
A = "adfg"
B = "dafs"
N = len(A)
M = len(B)
# Aのi文字目まで、Bのj文字目までの共通部分列(LCS)の最大値
dp = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + 1)
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
print(dp[-1][-1])
print(dp)

# 共通部分列の数え上げ
A = "abbbcca"
B = "abc"
N = len(A)
M = len(B)
dp = [[1] + [0 for _ in range(M)] for _ in range(N + 1)]
for i in range(N):
    for j in range(M):
        if A[i] == B[j]:
            dp[i + 1][j + 1] += dp[i][j]
        dp[i + 1][j + 1] += dp[i][j + 1]
print(dp[-1][-1])
print(dp)