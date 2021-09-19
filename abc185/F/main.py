#!/usr/bin/env python3
import sys

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
        self.tree[pos] ^= x
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

        print(left, self.N, condfunc(self.segquery(left, self.N)), self.segquery(left, self.N))
        # if impossible (ie. condfunc( func( A[left], ... , A[-1])) is False)
        if not condfunc(self.segquery(left, self.N)):
            return self.N
        
        # possible
        func_value = self.identityElement
        rightpos = left + self._seg_length_half - 1
        while True: 
            # while rightpos is the left-child, move bottom-up
            while rightpos&1 == 1:
                rightpos //= 2
            # try
            up_value_trial = self.func(func_value, self.tree[rightpos])
            if not condfunc(up_value_trial):
                # move up and right
                func_value = up_value_trial
                rightpos = (rightpos-1)//2 + 1
            else:
                # move top-down
                while rightpos < self._seg_length_half-1:
                    down_value_trial = self.func(func_value, self.tree[rightpos*2 + 1])
                    if condfunc(down_value_trial):
                        # move left-child
                        rightpos = rightpos*2 + 1
                    else:
                        # move right-child
                        func_value = down_value_trial
                        rightpos = rightpos*2 + 2
                return rightpos - self._seg_length_half + 1

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    st = SegmentTree(A, func=lambda a, b: a ^ b, identityElement=0)
    for _ in range(Q):
        C, x, y = map(int, input().split())
        if C == 1:
            st.pointupdate(x - 1, y)
        else:
            print(st.segquery(x - 1, y))
    return
    
if __name__ == '__main__':
    main()