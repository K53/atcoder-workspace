#!/usr/bin/env python3
import sys
from itertools import permutations

def main():
    N, K = map(int, input().split())
    T = []
    n = []
    for i in range(N):
        T.append(list(map(int, input().split())))
        n.append(i)
    
    ans = 0
    for root in permutations(range(1, N)):
        cost = 0
        now = 0
        for i in list(root) + [0]:
            cost += T[now][i]
            now = i
        if cost == K:
            ans += 1
    print(ans)
    return

    
if __name__ == '__main__':
    main()
