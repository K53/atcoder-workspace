#!/usr/bin/env python3
import sys
import math

def main():
    N, K = map(int, input().split())
    A = list(map(lambda i: int(i) - 1, input().split()))
    dv = []
    dv.append(A)
    for i in range(math.ceil(math.log2(K))):
        l = []
        for j in range(N):
            l.append(dv[i][dv[i][j]])
        dv.append(l)
    
    now = 0
    for i in range(math.ceil(math.log2(K))):
        if K >> i & 1:
            now = dv[i][now]
    print(now + 1)

        

if __name__ == '__main__':
    main()
