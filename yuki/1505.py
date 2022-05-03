#!/usr/bin/env python3
import sys

def main():
    # N, K = map(int, input().split())
    N = int(input())
    A = list(map(int, input().split()))
    nums = []
    c = 0
    for aa in A:
        if aa == 0:
            nums.append(c)
            c = 0
        else:
            c += 1
    nums.append(c)
    ans = (1 + N) * N // 2
    for i in nums:
        ans -= (1 + i) * i // 2
    print(ans)
    return
    


if __name__ == '__main__':
    main()