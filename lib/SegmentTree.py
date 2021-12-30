# ------------------------------------------------------------------------------
#     セグメント木 (0-indexed)
# ------------------------------------------------------------------------------
# 解説
# 根は 0 、頂点vの左の子は 2v + 1、右の子は 2v + 2
#
# リンク
# - https://juppy.hatenablog.com/entry/2019/05/02/%E8%9F%BB%E6%9C%AC_python_%E3%82%BB%E3%82%B0%E3%83%A1%E3%83%B3%E3%83%88%E6%9C%A8_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder
# 
# 計算量
# - pointUpdate()、pointAdd() : 要素の変更
# - segQuery() : 区間[l, r)に対する演算結果の取得
#   - O(2logN)
# - segSearchRight() : 
#   - ? 
# 
# verify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A&lang=ja
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja // Range Sum Query (RSQ)
# - https://atcoder.jp/contests/abc170/tasks/abc170_e
# - https://atcoder.jp/contests/abc185/tasks/abc185_f (XOR)
# - https://atcoder.jp/contests/abc157/tasks/abc157_e (OR)
# ------------------------------------------------------------------------------
class SegmentTree:
    def __init__(self, initVal: int, bottomLen: int, func: "function(int, int)"):
        self.initVal = initVal
        self.func = func
        self.bottomLen = bottomLen
        self.offset = self.bottomLen        # セグ木の最下層の最初のインデックスに合わせるためのオフセット
        self.segLen = self.bottomLen * 2
        self.tree = [initVal] * self.segLen

    """ 一点加算
    tree[index] += val
    """
    def pointAdd(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] += val # Add
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])
    
    """ 一点更新
    tree[index] = val
    """
    def pointUpdate(self, index: int, val: int):
        segIndex = index + self.offset
        self.tree[segIndex] = val # Update # 更新方法も変更が必要な場合は書き換えること。 eg.) XOR演算など |= val
        while True:
            segIndex //= 2
            if segIndex == 0:
                break
            self.tree[segIndex] = self.func(self.tree[segIndex * 2], self.tree[segIndex * 2 + 1])

    """ 区間最小値 (RMQ)
    """
    def rangeQuery(self, l: int, r: int):
        l += self.offset
        r += self.offset
        res = self.initVal
        while l < r:
            if l % 2 == 1:
                res = self.func(res, self.tree[l])
                l += 1
            l //= 2
            if r % 2 == 1:
                res = self.func(res, self.tree[r - 1])
                r -= 1
            r //= 2
        return res

# usage
# STEP.1) セグ木で使う関数を定義。セグ木初期化時にfuncとして食わせる。
# 二分木の各要素A, B, Cにおいて、A = f(B, C)の f() を定義。
#
#    A
#   / \
#  B   C
# 
def add(x: int, y: int):
    return x + y

# STEP.2) initValを定義。セグ木の各ノードの初期値。
# 演算に影響しないモノイドを指定。
# 加算 → 0
# 最小値 → INF など。
INF = 10 ** 9
tr = SegmentTree(initVal=0, bottomLen=2**18, func=add)

tr.pointAdd(1, 1)
tr.pointAdd(2, 2)
tr.pointAdd(3, 3)

# STEP.3) セグ木は右側は開区間として計算しているので+1必要。
print(tr.rangeQuery(1, 2 + 1))


# class SegmentTree:
#     def __init__(self, initList, identityElement, func):
#         assert (func(identityElement, identityElement) == identityElement)
#         self.N = len(initList)
#         self.initList = initList
#         self.identityElement = identityElement
#         self.func = func
#         self._seg_length_half = 2 ** ((self.N - 1).bit_length())
#         self.tree = [identityElement] * (2 * self._seg_length_half)
#         self._build()

#     def _build(self):
#         # Set value at the bottom
#         for i in range(self.N):
#             self.tree[i + self._seg_length_half - 1] = self.initList[i]    
#         # Build value
#         for i in range(self._seg_length_half - 2, -1, -1):
#             self.tree[i] = self.func(self.tree[2 * i + 1], self.tree[2 * i + 2])
    
#     def pointUpdate(self, k, x):
#         '''Update : A[k] = x '''
#         pos = k + self._seg_length_half - 1 # 末端のノードのインデックスに変換する処理
#         # Set value at k-th
#         self.tree[pos] = x
#         # Build bottom-up
#         while pos:
#             pos = (pos - 1) // 2
#             self.tree[pos] = self.func(self.tree[pos * 2 + 1], self.tree[pos * 2 + 2])
    
#     def pointAdd(self, k, x):
#         '''Update : A[k] = x '''
#         pos = k + self._seg_length_half - 1 # 末端のノードのインデックスに変換する処理
#         # Add value at k-th
#         self.tree[pos] += x
#         # Build bottom-up
#         while pos:
#             pos = (pos - 1) // 2
#             self.tree[pos] = self.func(self.tree[pos * 2 + 1], self.tree[pos * 2 + 2])
    
#     def pointGetVal(self, k):
#         ''' Return A[k] '''
#         return self.tree[k + self._seg_length_half - 1]

#     def segQuery(self, left, right):
#         ''' Return func(A[left], ... , A[right - 1]) '''
#         # if not left < right
#         if right <= left:
#             return self.identityElement
        
#         res = self.identityElement
#         leftpos = left + self._seg_length_half - 1 # leftmost segment
#         rightpos = right - 1 + self._seg_length_half - 1 # rightmost segment
#         print("[]", leftpos, rightpos, res)
#         while leftpos < rightpos-1:
#             if leftpos & 1 == 0: # 2で割り切れる=もう上には登れない(0-indexedなので)ので、resに追加。
#                 # if leftpos is right child
#                 res = self.func(res, self.tree[leftpos])
#             if rightpos & 1 == 1: # 2で割り切れない=もう上には登れない(0-indexedなので)ので、resに追加。
#                 # if rightpos is left child
#                 res = self.func(res, self.tree[rightpos])
#                 rightpos -= 1
#             # move up
#             leftpos = leftpos // 2
#             rightpos = (rightpos-1) // 2
#             print("[]", leftpos, rightpos, res)
        
#         res = self.func(res, self.tree[leftpos])
#         if leftpos != rightpos:
#             res = self.func(res, self.tree[rightpos])
#         return res

#     def segSearchRight(self, condfunc, left = 0):
#         ''' Return min_i satisfying condfunc( func( A[left], ... , A[i])) 
#         if impossible : return -1
#         '''
#         # if impossible (ie. condfunc( func( A[left], ... , A[-1])) is False)
#         if not condfunc(self.segQuery(left, self.N)):
#             return -1
        
#         # possible
#         func_value = self.identityElement
#         rightpos = left + self._seg_length_half - 1
#         while True: 
#             # while rightpos is the left-child, move bottom-up
#             while rightpos & 1 == 1:
#                 rightpos //= 2
#             # try
#             up_value_trial = self.func(func_value, self.tree[rightpos])
#             if not condfunc(up_value_trial):
#                 # move up and right
#                 func_value = up_value_trial
#                 rightpos = (rightpos - 1) // 2 + 1
#             else:
#                 # move top-down
#                 while rightpos < self._seg_length_half - 1:
#                     down_value_trial = self.func(func_value, self.tree[rightpos * 2 + 1])
#                     if condfunc(down_value_trial):
#                         # move left-child
#                         rightpos = rightpos * 2 + 1
#                     else:
#                         # move right-child
#                         func_value = down_value_trial
#                         rightpos = rightpos * 2 + 2
#                 return rightpos - self._seg_length_half + 1

#     def __str__(self):
#         cnt = 0
#         res = []
#         for i in range((self.N - 1).bit_length() + 1):
#             num = 2 ** i
#             res.append(" ".join(f'{j}' for j in self.tree[cnt:cnt + num]))
#             cnt += num
#         return "\n".join(res)

# # usage
# A = [2, 6, 1, 8, 5, 5, 0, 3]
# st = SegmentTree(initList=A, func=max, identityElement=0) # 最大値でセグ木構築
# # 最小値 → SegmentTree(initList=[], func=min, identityElement=INF)
# # or演算 → SegmentTree(initList=[], func=lambda a, b : a | b, identityElement=0)
# # xor演算 → SegmentTree(initList=[], func=lambda a, b : a ^ b, identityElement=0)
# print(st.tree)
# "-> [8, 8, 5, 6, 8, 5, 3, 2, 6, 1, 8, 5, 5, 0, 3, 0]"
# print("---")
# print(st)
# """
# -> 8
# -> 8 5
# -> 6 8 5 3
# -> 2 6 1 8 5 5 0 3
# """
# """
# -> |            0               |
# -> |     1      |       2       |
# -> |  3  |   4  |   5   |   6   |
# -> | 7 8 | 9 10 | 11 12 | 13 14 |
# """
# print("---")

# print(st.segQuery(0, 6)) # 区間A[0]〜A[2]の最大値
# "-> 6" # A[3]=8は含まないので注意。

# def judge(i):
#     return i >= 7
# print(st.segSearchRight(condfunc=judge, left=0)) # 0を始点として初めてjudge()を満たす区間。(=最大値が7以上を最小の区間)
# "-> 3" # A[0]〜A[3]までで初めてjudge()を満たす。(=7を超える最小の区間がA[0]〜A[3]。)


