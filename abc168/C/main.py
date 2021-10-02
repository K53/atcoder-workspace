#!/usr/bin/env python3
import sys
import math

def main():
    A, B, H, M = map(int, input().split())
    # 6 /min
    # 0.5 /min
    mm = H * 60 + M
    digree = min(5.5 * mm, 360 - 5.5 * mm)
    print((A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(digree))) ** 0.5)

if __name__ == '__main__':
    main()
