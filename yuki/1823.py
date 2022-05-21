#!/usr/bin/env python3
import sys
MOD = 998244353
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        S = sum(A)
        if S % 3 != 0:
            print("No")
            continue
        if max(A) > S // 3:
            print("No")
            continue
        print("Yes")
    return

if __name__ == '__main__':
    main()