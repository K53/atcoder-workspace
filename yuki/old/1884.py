#!/usr/bin/env python3
import sys
import math

def main():
    N = int(input())
    A = list(map(int, input().split()))
    aa = []
    zero = 0
    for i in A:
        if i != 0:
            aa.append(i)
        else:
            zero += 1
    aa.sort()
    diff = []
    g = 0
    for i in range(len(aa) - 1):
        diff.append(aa[i + 1] - aa[i])
        g = math.gcd(g, aa[i + 1] - aa[i])

    if 0 in diff and g != 0:
        print("No")
        return
    if g == 0:
        print("Yes")
        return
    ans = 0
    for d in diff:
        ans += d // g - 1
    if ans <= zero:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()