#!/usr/bin/env python3
import sys
YES = "Yes"  # type: str
NO = "No"  # type: str

input = lambda: sys.stdin.readline().strip()
def main():
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = set(map(int, input().split()))
    X = int(input())

    dp = [0] * (X + 1)
    dp[0] = 1
    for i in range(X + 1):
        if dp[i] == 0:
            continue
        for aa in A:
            if i + aa > X or (i + aa) in B:
                continue
            dp[i + aa] = 1
    print(NO if dp[X] == 0 else YES)
    return


if __name__ == '__main__':
    main()
