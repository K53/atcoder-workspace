#!/usr/bin/env python3
import sys

def getLengthOfLcs(a: str, b: str):
    L = []
    for bk in b:
        bgn_idx = 0  # 検索開始位置
        for i, cur_idx in enumerate(L):
            # ※1
            chr_idx = a.find(bk, bgn_idx) + 1
            if not chr_idx:
                break
            L[i] = min(cur_idx, chr_idx)
            bgn_idx = cur_idx
        else:
            # ※2
            chr_idx = a.find(bk, bgn_idx) + 1
            if chr_idx:
                L.append(chr_idx)
    return len(L)
 
def main():
    q = int(input())
    for _ in range(q):
        s = input()
        t = input()
        print(getLengthOfLcs(s, t))

if __name__ == '__main__':
    main()
