#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    dp = 1 # 和がkのものが何個あるか (mod2) -> 最初は和0が1個のみ
    for aa in A:
        dp ^= (dp << aa)
        # print(bin(dp))
    ans = 0
    d = str(bin(dp))[2:]
    for i in range(len(d)):
        if int(d[i]):
            ans ^= i
            # print(ans)
    print(ans)


if __name__ == '__main__':
    main()