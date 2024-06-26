# ------------------------------------------------------------------------------
#     Imos法 (いもす法)
# ------------------------------------------------------------------------------
# 
# verify
# - https://atcoder.jp/contests/abc221/tasks/abc221_d (座圧いもす)
# ------------------------------------------------------------------------------

N = 5
S = [1,2,3,4,5]
T = [4,5,6,7,8]
# テーブルの初期化
maxST = 2 * 10 ** 5
imos = [0] * (maxST + 1)
for i in range(N):
    imos[S[i]] += 1
    imos[T[i] + 1] -= 1

# ビルド
for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

# ------------------------------------------------------------------------------
#     木上のImos法 (木上のいもす法)
# ------------------------------------------------------------------------------
# 木のいもす法
#
# verify
# - https://atcoder.jp/contests/abc183/tasks/abc183_d
# ------------------------------------------------------------------------------

N = 5
a = [1, 2, 2, 3]
b = [2, 3, 4, 5]
imos = [0] * N

# グラフ構築
G = [[] for _ in range(N)]
for i in range(N - 1):
    G[a[i] - 1].append(b[i] - 1)
    G[b[i] - 1].append(a[i] - 1)

# テーブルの初期化 : S[i]を根とする部分木に加算。
S = [1,3]
for i in range(len(S)):
    imos[S[i] - 1] += 1

# ビルド
from collections import deque
q = deque()
q.append((-1, 0))
while q:
    pre, cur = q.popleft()
    for next in G[cur]:
        if pre == next:
            continue
        q.append((cur, next))
        imos[next] += imos[cur]

print(*imos) # 1 1 2 1 2

# ------------------------------------------------------------------------------
#     座標圧縮 + Imos法 (いもす法)
# ------------------------------------------------------------------------------
# 
# verify
# - https://atcoder.jp/contests/abc221/tasks/abc188_d (座圧いもす)
# ------------------------------------------------------------------------------

N = 5
S = [4,14,31,532,2341]
T = [12,17,1798,5069,8213]

# 圧縮
endT = [bb + 1 for bb in T]
L = S + endT
raw_to_compressed = {}
compressed_to_raw = []
for index, val in enumerate(sorted(list(set(L)))):
    raw_to_compressed[val] = index
    compressed_to_raw.append(val)

# テーブルの初期化
imos = [0] * len(compressed_to_raw)
for i in range(N):
    imos[raw_to_compressed[S[i]]] += 1
    imos[raw_to_compressed[endT[i]]] -= 1
    
# ビルド
for i in range(1, len(imos)):
    imos[i] += imos[i - 1]

# 値の復元
# いもす配列上でのi番目を圧縮前の値に復元した時の次の要素までの範囲。
# original       4,    13,   14 
#       ↓             (12+1)
#       ↓
# compressed(i)  0,     1,    2
#                ↓
#               この0の期間は original[i + 1] - original[i] の期間。
#               すなわち、compressed_to_raw[i + 1] - compressed_to_raw[i]
for i in range(len(compressed_to_raw) - 1):
    value_on_imos = imos[i] # imosテーブル上の値
    span = compressed_to_raw[i + 1] - compressed_to_raw[i] # その値をとり続ける実際の値の長さ