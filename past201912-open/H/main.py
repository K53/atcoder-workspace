#!/usr/bin/env python3


import heapq


if __name__ == '__main__':
    N = int(input())
    C = list(map(int, input().split()))
    Q = int(input())
    odd = 0
    all = 0
    ans = 0
    for _ in range(Q):
        S = list(map(int, input().split()))
        if S[0] == 1:
            x, a = S[1] - 1, S[2]
            rest = C[x] - all - odd if x % 2 == 0 else C[x] - all # 0-index
            if rest >= a:
                C[x] -= a
                ans += a
        elif S[1] == 2:
            # if 
            odd += S[1]
            ans += S[1] * (N + 1) // 2
        else:
            all += S[1]
            ans += S[1] * N
        print(ans)



