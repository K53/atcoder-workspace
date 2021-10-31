#!/usr/bin/env python3
import sys

def main():
    T = int(input())
    for _ in range(T):
        K = int(input())
        a = [0] * K
        a[0] = 2 % K
        if a[0] == 0:
            print(1)
            continue
        for i in range(1, K):
            a[i] = (a[i - 1] * 10 + 2 ) % K
            if a[i] == 0:
                print(i + 1)
                break
        else:
            print(-1)

if __name__ == '__main__':
    main()
