#!/usr/bin/env python3
from itertools import accumulate
import bisect

# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    # N = 3
    # A = [0, 480, 600]
    rA = []
    frm = 0
    for i in range(N):
        if i % 2 == 0:
            rA.append(A[i] - frm)
        else:
            frm = A[i]
            rA.append(0)
    # print(A)
    # print(rA)
    revrA = rA[::-1]
    # print(revrA)
    accrA = list(accumulate(rA))
    accrevrA = list(accumulate(revrA))
    # print(accrA)
    # print(accrevrA)
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        # l = 550
        # r = 600
        # l = 120
        l_idx = bisect.bisect_left(A, l)
        if l_idx % 2 != 0:
            l = A[l_idx]
            r_idx = l_idx + 1
        # print(l_idx)
        # print(l, l_idx)
        # print(A[l_idx] - l) # 含む分
        # print(accrA[l_idx]) # 除く分
        # print(accrA[-1] - accrA[l_idx] + A[l_idx] - l)
        tot = accrA[-1] - accrA[l_idx] + A[l_idx] - l
        # r = 1450
        r_idx = bisect.bisect_left(A, r)
        if r_idx % 2 != 0:
            r = A[r_idx - 1]
            r_idx = r_idx - 1
        # print(r, r_idx)
        # print(N - r_idx)
        # print(r - A[r_idx - 1]) # 含む分
        # print(accrevrA[N - r_idx]) # 除く分
        # print(accrevrA[N - r_idx] - (r - A[r_idx - 1])) # 含む分
        if r_idx == 0:
            print(0)
            continue
        tot -= accrevrA[N - r_idx] - (r - A[r_idx - 1])
        print(tot)


        # break
        


if __name__ == '__main__':
    main()
