#! /usr/bin/env python
import sys
sys.setrecursionlimit(10**9)

def wrap():
    N = int(input())
    if N == 0:
        exit(0)
    *W, = map(int,input().split())
    dp = [[-1] * (N + 1) for _ in range(N + 1)]
    def f(l, r):
        if dp[l][r] != -1:
            return dp[l][r]
        
        if r - l <= 1: # 両端が同じものを指している
            dp[l][r] = 0
            return 0
        if r - l == 2: # rを含まないなので lとl+1しかない
            if abs(W[l] - W[l + 1]) <= 1:
                dp[l][r] = 2
                return 2
            else:
                dp[l][r] = 0
                return 0

        # 全部取り除けるなら両端が消せる
        if f(l + 1, r - 1) == r - l - 2:
            if abs(W[l] - W[r - 1]) <= 1:
                dp[l][r] = max(dp[l][r], r - l)
        
        for mid in range(l + 1, r - 1 + 1):
            dp[l][r] = max(dp[l][r], f(l, mid) + f(mid, r))
        
        return dp[l][r]
    print(f(0, N))
    print(dp)

def main():
    while True:
        wrap()
    

if __name__ == "__main__":
    main()
