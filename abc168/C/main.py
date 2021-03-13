#!/usr/bin/env python3
import sys
import math

def main():
    A, B, H, M = map(int, input().split())
    h = 0.5 * (H * 60 + M)
    m = 6 * M
    dig = abs(h - m)
    print(math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(math.radians(dig))))

if __name__ == '__main__':
    main()
