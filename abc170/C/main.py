#!/usr/bin/env python3
import sys

def main():
    X, N = map(int, input().split())
    p = list(map(int, input().split())) if N != 0 else []
    for d in range(X + 1):
        for v in [-1, 1]:
            a = X + d * v
            if p.count(a) == 0:
                print(a)
                return



if __name__ == '__main__':
    main()
