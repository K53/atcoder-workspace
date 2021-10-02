# ------------------------------------------------------------------------------
#     セグメント木
# ------------------------------------------------------------------------------
# 解説
#
# リンク
# - https://juppy.hatenablog.com/entry/2019/05/02/%E8%9F%BB%E6%9C%AC_python_%E3%82%BB%E3%82%B0%E3%83%A1%E3%83%B3%E3%83%88%E6%9C%A8_%E7%AB%B6%E6%8A%80%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0_Atcoder
# 
# 計算量
# - pointupdate() : 要素の変更
# - segquery() : 区間[l, r)に対する演算結果の取得
#   - O(logN)
# 
# Modify
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A&lang=ja
# - https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B&lang=ja
# ------------------------------------------------------------------------------
class SegmentTree:
    def __init__(self, initList, identityElement, func):
        assert (func(identityElement, identityElement) == identityElement)
        self.N = len(initList)
        self.initList = initList
        self.identityElement = identityElement
        self.func = func
        self._seg_length_half = 2 ** ((self.N - 1).bit_length())
        self.tree = [identityElement] * (2 * self._seg_length_half)
        self._build()

    def _build(self):
        # Set value at the bottom
        for i in range(self.N):
            self.tree[i + self._seg_length_half - 1] = self.initList[i]    
        # Build value
        for i in range(self._seg_length_half - 2, -1, -1):
            self.tree[i] = self.func(self.tree[2 * i + 1], self.tree[2 * i + 2])
    
    def pointupdate(self, k, x):
        '''Update : A[k] = x '''
        pos = k + self._seg_length_half - 1
        # Set value at k-th
        self.tree[pos] = x
        # Build bottom-up
        while pos:
            pos = (pos - 1) // 2
            self.tree[pos] = self.func(self.tree[pos * 2 + 1], self.tree[pos * 2 + 2])
    
    def pointgetval(self, k):
        ''' Return A[k] '''
        return self.tree[k + self._seg_length_half - 1]

    def segquery(self, left, right):
        ''' Return func(A[left], ... , A[right-1]) '''
        # if not left < right
        if right <= left:
            return self.identityElement
        
        res = self.identityElement
        leftpos = left + self._seg_length_half - 1 # leftmost segment
        rightpos = right - 1 + self._seg_length_half - 1 # rightmost segment

        while leftpos < rightpos-1:
            if leftpos & 1 == 0:
                # if leftpos is right-child
                res = self.func(res, self.tree[leftpos])
            if rightpos & 1 == 1:
                # if rightpos is leftchild
                res = self.func(res, self.tree[rightpos])
                rightpos -= 1
            # move up
            leftpos = leftpos // 2
            rightpos = (rightpos-1) // 2
        
        res = self.func(res, self.tree[leftpos])
        if leftpos != rightpos:
            res = self.func(res, self.tree[rightpos])
        return res

    def segsearch_right(self, condfunc, left = 0):
        ''' Return min_i satisfying condfunc( func( A[left], ... , A[i])) 
        if impossible : return n
        '''
        # if impossible (ie. condfunc( func( A[left], ... , A[-1])) is False)
        if not condfunc(self.segquery(left, self.N)):
            return self.N
        
        # possible
        func_value = self.identityElement
        rightpos = left + self._seg_length_half - 1
        while True: 
            # while rightpos is the left-child, move bottom-up
            while rightpos & 1 == 1:
                rightpos //= 2
            # try
            up_value_trial = self.func(func_value, self.tree[rightpos])
            if not condfunc(up_value_trial):
                # move up and right
                func_value = up_value_trial
                rightpos = (rightpos - 1) // 2 + 1
            else:
                # move top-down
                while rightpos < self._seg_length_half - 1:
                    down_value_trial = self.func(func_value, self.tree[rightpos * 2 + 1])
                    if condfunc(down_value_trial):
                        # move left-child
                        rightpos = rightpos * 2 + 1
                    else:
                        # move right-child
                        func_value = down_value_trial
                        rightpos = rightpos * 2 + 2
                return rightpos - self._seg_length_half + 1

    def __str__(self):
        cnt = 0
        res = []
        for i in range((st.N - 1).bit_length() + 1):
            num = 2 ** i
            res.append(" ".join(f'{j}' for j in st.tree[cnt:cnt + num]))
            cnt += num
        return "\n".join(res)

# usage
A = [2, 6, 1, 8, 5, 5, 0, 3]
st = SegmentTree(initList=A, func=max, identityElement=0) # 最大値でセグ木構築
print(st.tree)
"-> [8, 8, 5, 6, 8, 5, 3, 2, 6, 1, 8, 5, 5, 0, 3, 0]"
print("---")
print(st)
"""
-> 8
-> 8 5
-> 6 8 5 3
-> 2 6 1 8 5 5 0 3
"""
print("---")

print(st.segquery(0, 3)) # 区間A[0]〜A[2]の最大値
"-> 6" # A[3]=8は含まないので注意。

def judge(i):
    return i >= 7
print(st.segsearch_right(condfunc=judge, left=0)) # 0を始点として初めてjudge()を満たす区間。(=最大値が7以上を最小の区間)
"-> 3" # A[0]〜A[3]までで初めてjudge()を満たす。(=7を超える最小の区間がA[0]〜A[3]。)


