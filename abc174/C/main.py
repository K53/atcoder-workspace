#!/usr/bin/env python3
import sys

def main():
    K = int(input())
    a = [0] * K
    a[0] = 7 % K
    if a[0] == 0:
        print(1)
        return
    for i in range(1, K):
        a[i] = (a[i - 1] * 10 + 7 ) % K
        if a[i] == 0:
            print(i + 1)
            return
    print(-1)

if __name__ == '__main__':
    main()
