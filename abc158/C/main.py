#!/usr/bin/env python3
import sys
import math

def main():
    A, B = map(int, input().split())
    for i in range(10 ** 5):
        tax8 = math.floor(i * 0.08)
        tax10 = math.floor(i * 0.1)
        if tax8 == A and tax10 == B:
            print(i)
            return
        if tax8 > A and tax10 > B:
            print(-1)
            return
    return

if __name__ == '__main__':
    main()
