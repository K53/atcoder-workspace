# ------------------------------------------------------------------------------
#     尺取り法
# ------------------------------------------------------------------------------
# verify
# - https://atcoder.jp/contests/abc032/tasks/abc032_c 
# - https://atcoder.jp/contests/abc130/tasks/abc130_d
# ------------------------------------------------------------------------------

# 一般化されたスニペット
r = 0
l = 0
ans = 0
mul = 1
for _ in range(N):
    # 行けるだけrを進める。sumが条件を満たさなくなったところで抜ける。※抜ける時、条件を満たさなくなったrの次を指している。
    while r < N and "rを右へ進める条件":
        # print("#", l, r, mul)
        mul *= S[r]
        r += 1
    # → 条件を満たしていない状態をlを進めることで修正する。
    # ifの前でansに対する更新を試みてはいけない理由→この時点では条件を満たしていないから。
    # ifを構えるのはwhileを抜ける理由がrの上限だった場合。lを縮める必要がないから。
    if l == r:
        l += 1
        r += 1
        continue
    if "lを左へ進める条件":
        # print(">", l, r, mul) # rを含まないのでr=N+1までは来る。
        mul //= S[l]
        l += 1
        ans = max(ans, r - l)
ans = max(ans, r - l) # 一度もlを縮めることがないケースではansに到達しないため最後にansの更新を入れる必要あり。 ansがlに依存する問題では入れること。
print(ans)

# ------------------------------------------------------------------------------

# https://atcoder.jp/contests/abc032/tasks/abc032_c
# 連続する部分数列の積がK以下となる最大長の算出。
S = [4, 3, 1, 1, 2, 10, 2]
N = len(S)
K = 6
r = 0
l = 0
ans = 0
mul = 1
for _ in range(N):
    # 行けるだけrを進める。sumが条件を満たさなくなったところで抜ける。※抜ける時、条件を満たさなくなったrの次を指している。
    while r < N and mul <= K:
        # print("#", l, r, mul)
        mul *= S[r]
        r += 1
    # → 条件を満たしていない状態をlを進めることで修正する。
    # ifの前でansに対する更新を試みてはいけない理由→この時点では条件を満たしていないから。
    # ifを構えるのはwhileを抜ける理由がrの上限だった場合。lを縮める必要がないから。
    if l == r:
        l += 1
        r += 1
        continue
    if mul > K:
        # print(">", l, r, mul) # rを含まないのでr=N+1までは来る。
        mul //= S[l]
        l += 1
        ans = max(ans, r - l)
ans = max(ans, r - l) # 一度もlを縮めることがないケースではansに到達しないため最後にansの更新を入れる必要あり。 ansがlに依存する問題では入れること。
print(ans)


# https://atcoder.jp/contests/abc130/tasks/abc130_d
# 連続する部分列の和がK以上の両端の部分列の個数。
a = [6, 1, 2, 7]
N = len(a)
K = 10
r = 0
l = 0
ans = 0
sum = 0
for _ in range(N):
    # 行けるだけrを進める。sumが条件を満たさなくなったところで抜ける。※抜ける時、条件を満たさなくなったrの次を指している。
    # sum=[6] l=0, r=1 で抜ける
    # sum=[6, 1] l=0, r=2 で抜ける
    # sum=[6, 1, 2] l=0, r=3 で抜ける
    # sum=[6, 1, 2, 7] l=0, r=4 で抜ける <- K=10の今回はこの状態で抜けてくる。つまり、以下
    ### 条件を満たすのは区間[0,2]でsum=[6, 1, 2] → l=0, r=3
    ### 条件を満たさなくなった区間[0,3]でsum=[6, 1, 2, 7] l=0, r=4
    ### [0,2]とl=0, r=4を混同注意。ズレが2つ分あるわけではない。
    while r < N and sum < K:
        print("#", l, r, sum)
        sum += a[r]
        r += 1
    # → 条件を満たしていない状態をlを進めることで修正する。
    # ifの前でansに対する更新を試みてはいけない理由→この時点では条件を満たしていないから。
    # ifを構えるのはwhileを抜ける理由がrの上限だった場合。lを縮める必要がないから。
    if l == r:
        l += 1
        r += 1
        continue
    if sum >= K:
        print(">", l, r, sum) # rを含まないのでr=N+1までは来る。
        sum -= a[l]
        l += 1
        ans += N - r + 1
# 一度もlを縮めることがないケースではansに到達しないため最後にansの更新を入れる必要あり。 
# 今回 ans += N - r + 1 はlに依存しないのでここでの調整は不要。
print(ans)


# https://atcoder.jp/contests/abc038/tasks/abc038_c
# 単調増加な区間の個数。
a = a + [-100]
N += 1
l = 0
r = 1 # <- 初期値を崩すケースもある。
ans = 0
for _ in range(N):
    while r < N and a[r - 1] < a[r]:
        print("#", l, r, a[l:r])
        r += 1
    if r < N and a[r - 1] >= a[r]:
        print(">", l, r, a[l:r])
        num = r - 1 - l + 1
        ans += num * (num + 1) // 2
        l = r  # lをちまちま進めないで一気にrまで引き上げる。
        r += 1 # rは1歩進めてあげる。
print(ans)



## 検証中
# こっちの方がわかりやすいかもしれない。

l = 0 # 含む → 区間短縮時、移動元を引く
r = 0 # 含まない → 区間拡張時、移動元を足す
ans = 0
count = 0
for _ in range(N):
    while r < N:
        # print("#", l, r, count)
        if S[r][0] == "0":
            if K == 0: 
                break
            count += S[r][1]
            r += 1
            K -= 1
        else:
            count += S[r][1]
            r += 1
    if l == r: # rが一歩も進まなかったらその要素は無視してlもrも先に進まませる。
        l += 1
        r += 1
        continue
    ans = max(ans, count)
    if S[l][0] == "0":
        count -= S[l][1]
        l += 1
        K += 1
    else:
        count -= S[l][1]
        l += 1
    # print(">", l, r, count)
ans = max(ans, count) # 一度もlを縮めることがないケースではansに到達しないため最後にansの更新を入れる必要あり。 ansがlに依存する問題では入れること。
print(ans)