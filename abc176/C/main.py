#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = list(map(int, input().split()))
    h = 0
    ans = 0
    for i in A:
        if h <= i:
            h = i
            continue
        ans += h - i
    print(ans)
    return
    
if __name__ == '__main__':
    main()
