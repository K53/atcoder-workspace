#!/usr/bin/env python3
import sys

def divPolynomial(dividend: "list[int]", divisor: "list[int]"):
    N = dividend
    M = divisor
    # 割る数の方が割られる数よりも高次数の場合を弾く。
    if N < M:
        return 0, dividend
    p, q = [], []
    prev_carried = 0
    for j in reversed(range(N)):
        for k in reversed(range(M)): 
        next_carry = (dividend[j] - prev_carried * -x_i) // divisor[k]
        p.append(next_carry)
        prev_carried = next_carry
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    last_xors = 0
    xors = set([last_xors])
    for aa in A:
        last_xors ^= aa
        target = last_xors ^ K
        if target in xors:
            print("Yes")
            return
        xors.add(last_xors)
    print("No")
    return
        
if __name__ == '__main__':
    main()