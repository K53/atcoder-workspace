#!/usr/bin/env python3
import sys
class BIT:
    def __init__(self, N):
        self.N = N
        self.tree = [0] * (self.N + 1) # 1-indexedのため
        
    def add(self, pos, val):
        '''Add : A[pos] = val '''
        i = pos + 1 # convert from 0-index to 1-index
        while i <= self.N:
            self.tree[i] += val
            i += i & -i

    def sum(self, pos):
        ''' Return Sum(A[1], ... , A[pos])'''
        res = 0
        i = pos + 1 # convert from 0-index to 1-index
        while i > 0:
            res += self.tree[i]
            # res %= MOD
            i -= i & -i    
        return res

def main():
    N, Q = map(int, input().split())
    bit = BIT(N)
    for _ in range(Q):
        C, x, y = map(int, input().split())
        if C == 0:
            bit.add(x - 1, y)
        else:
            print(bit.sum(y - 1) - bit.sum(x - 1 - 1))
    return
    
if __name__ == '__main__':
    main()