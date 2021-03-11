#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    ab = N - 1
    ans = 0
    for a in range(1, N):
        max_b = ab // a
        ans += max_b
    print(ans)
    return

if __name__ == '__main__':
    main()
