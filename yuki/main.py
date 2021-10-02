#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    
    for i in range(N - 1):
        if A[i + 1] - A[i] == 1:
            print(2)
            return
    print(1)
    return


if __name__ == '__main__':
    main()