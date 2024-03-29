#!/usr/bin/env python3
from collections import defaultdict
import sys
class BIT:
    def __init__(self, N):
        self.N = N
        self.bit = [0] * (self.N + 1) # 1-indexedのため
        
    def add(self, pos, val):
        '''Add
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            A[pos] += val 
        '''
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.bit[i] += val
            i += i & -i

    def sum(self, pos):
        ''' Sum
            O(logN)
            posは0-index。内部で1-indexedに変換される。
            Return Sum(A[0], ... , A[pos])
        '''
        res = 0
        i = pos + 1 # convert from 0-index to 1-index
        while i > 0:
            res += self.bit[i]
            i -= i & -i    
        return res
    
    def lowerLeft(self, w):
        '''
        O(logN)
        A0 ~ Aiの和がw以上となる最小のindex(値)を返す。
        Ai ≧ 0であること。
        '''
        if (w < 0):
            return 0
        total = self.sum(self.N - 1)
        if w > total:
            return -1
        x = 0
        k = 1 << (self.N.bit_length() - 1)
        while k > 0:
            if x + k < self.N and self.bit[x + k] < w:
                w -= self.bit[x + k]
                x += k
            k //= 2
        return x
        
    def __str__(self):
        '''
        index0は不使用なので表示しない。
        '''
        return "[" + ", ".join(f'{v}' for v in self.bit[1:]) + "]"

# import bisect
def solve(N: int, C: "List[int]", X: "List[int]"):
    bit = BIT(N + 1)
    ans = 0
    for i in range(N):
        val = X[i]
        # print(bit.bit[1:])
        # print(val, ":",  bit.sum(val)) # 今の位置iよりも左側に、今の位置の数valよりも大きい数は何個あるか。
        ans += i - bit.sum(val) 
        bit.add(val, 1)
    # print(ans)

    col = dict()
    for i in range(N):
        if C[i] in col:
            col[C[i]].append(X[i])
        else:
            col[C[i]] = [X[i]]

    res = 0
    bbb = BIT(N + 1)
    for cc, ll in col.items():
        for i in range(len(ll)):
            val = ll[i]
            # print(val, ":",  bbb.sum(val)) # 今の位置iよりも左側に、今の位置の数valよりも大きい数は何個あるか。
            res += i - bbb.sum(val) 
            bbb.add(val, 1)
            # print(bbb.bit[1:])
        for i in range(len(ll)):
            val = ll[i]
            bbb.add(val, -1)
        # print(res)

    print(ans - res)

    # nums = dict() 
    # res = 0
    # for i in range(N):
    #     if C[i] in nums:
    #         l = C[i]
    #         res += len(l) - bisect.bisect_right(l, X[i])

    #     else:
    #         C[i] = [X[i]]
    # print(res)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    X = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C, X)

if __name__ == '__main__':
    main()
