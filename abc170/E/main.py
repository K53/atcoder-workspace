#!/usr/bin/env python3
import sys
INF = 10 ** 16


import heapq
from collections import defaultdict
class HeapDict:
    def __init__(self):
        self.q=[]
        self.d=defaultdict(int)

    def insert(self, x):
        """insert x to queue"""
        heapq.heappush(self.q, x)
        self.d[x] += 1

    def erase(self, x):
        """erase x from queue"""
        if self.d[x] == 0:
            print(x, "is not in HeapDict")
            return
        else:
            self.d[x] -= 1

        while len(self.q) != 0:
            if self.d[self.q[0]] == 0:
                heapq.heappop(self.q)
            else:
                break
    
    def size(self):
        return sum(self.d.values())

    def exist(self, x):
        return self.d[x] != 0
    
    def getExistList(self):
        return [i for i in self.q if self.exist(i)]

    def dryPop(self):
        return self.q[0] if len(self.q) != 0 else -INF

    def __str__(self):
        return "[" + ", ".join([str(i) if self.exist(i) else "({})".format(i) for i in self.q]) + "]"

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
        if impossible : return -1
        '''
        # if impossible (ie. condfunc( func( A[left], ... , A[-1])) is False)
        if not condfunc(self.segquery(left, self.N)):
            return -1
        
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
        for i in range((self.N - 1).bit_length() + 1):
            num = 2 ** i
            res.append(" ".join(f'{j}' for j in self.tree[cnt:cnt + num]))
            cnt += num
        return "\n".join(res)


def solve(N: int, Q: int, A: "List[int]", B: "List[int]", C: "List[int]", D: "List[int]"):
    kind = 2 * 10 ** 5
    A = [-i for i in A]
    B = [i - 1 for i in B]
    C = [i - 1 for i in C]
    D = [i - 1 for i in D]
    hd = [HeapDict() for _ in range(kind)]

    for score, now in zip(A, B):
        hd[now].insert(score)
    
    maxs = [-h.dryPop() for h in hd]
    st = SegmentTree(initList=maxs, func=min, identityElement=INF)

    # for i in range(kind):
    #     print(hd[i], hd[i].size())
    # print("---")
    for num, to in zip(C, D):
        hd[B[num]].erase(A[num])
        st.pointupdate(B[num], -hd[B[num]].dryPop())
        hd[to].insert(A[num])
        B[num] = to
        st.pointupdate(to, -hd[B[num]].dryPop())
        print(st.segquery(0, kind))
        # print(st)
    
        # for i in range(kind):
        #     print(hd[i], hd[i].size())
        # print("-----")
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    C = [int()] * (Q)  # type: "List[int]"
    D = [int()] * (Q)  # type: "List[int]"
    for i in range(Q):
        C[i] = int(next(tokens))
        D[i] = int(next(tokens))
    solve(N, Q, A, B, C, D)

if __name__ == '__main__':
    main()
