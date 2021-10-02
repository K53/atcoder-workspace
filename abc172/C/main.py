#!/usr/bin/env python3
import sys
from itertools import accumulate
import bisect

def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Sa = [0] + list(accumulate(A))
    Sb = list(accumulate(B))
    ans = 0
    for aa in range(N + 1):
        rest = K - Sa[aa]
        if rest < 0:
            break
        bb = bisect.bisect_right(Sb, rest)
        ans = max(ans, aa + bb)
    print(ans)
    return
    



if __name__ == '__main__':
    main()
