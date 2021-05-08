#!/usr/bin/env python3
import sys
INF = 10 ** 18 + 1

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
 
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r + 1):                    # p番目について、
        pivot = denominator[p - 1]              # pivotで約分を試みる。
        if pivot > 1:                           # ただし、pivotが1、すなわちすでに割り尽くされているならp番目は飛ばす。
            offset = (n - r) % p
            for k in range(p-1,r,p):            # p番目を約分できるということはp番目からpの倍数番目も約分可能なので実施する。
                numerator[k - offset] //= pivot
                denominator[k] //= pivot
 
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result

def solve(N: int, K: int):
    # False - ng - ok - True
    def is_ok(mid: int):
        # 判定する条件
        if mid < 0:
            return False
        elif mid >= INF:
            return True
        
        return cmb(mid, 3) >= K 
    
    def binSearch(ok: int, ng: int):
        # print(ok, ng)
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
            # print(ok, ng, mid)
        return ok

    print(binSearch(INF, 0))
    return


# Generated by 2.2.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    solve(N, K)

if __name__ == '__main__':
    main()