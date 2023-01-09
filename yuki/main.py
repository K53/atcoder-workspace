#!/usr/bin/env python3
import sys

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    last_xors = 0
    xors = set([last_xors])
    for aa in A:
        last_xors ^= aa
        target = last_xors ^ K
        if target in xors:
            print("Yes")
            return
        xors.add(last_xors)
    print("No")
    return
        
if __name__ == '__main__':
    main()