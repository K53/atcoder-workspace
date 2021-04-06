#!/usr/bin/env python3
import sys

# def getLengthOfLcs(a: str, b: str):
#     L = []
#     for bk in b:
#         bgn_idx = 0  # 検索開始位置
#         for i, cur_idx in enumerate(L):
#             # ※1
#             chr_idx = a.find(bk, bgn_idx) + 1
#             if not chr_idx:
#                 break
#             L[i] = min(cur_idx, chr_idx)
#             bgn_idx = cur_idx
#         else:
#             # ※2
#             chr_idx = a.find(bk, bgn_idx) + 1
#             if chr_idx:
#                 L.append(chr_idx)
#     return len(L)

def primeFactrization(n: int) -> list:
    primeFactors = list()
    i = 2
    while i * i <= n:
        while n % i == 0:
            primeFactors.append(i)
            n //= i
        i += 1
    if n != 1:
        primeFactors.append(n)
    return primeFactors

def main():
    n = int(input())
    for t in enumerate(primeFactrization(n))
    print(s)
    

if __name__ == '__main__':
    main()
