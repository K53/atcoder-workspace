#!/usr/bin/env python3
import sys

def main():
    A, B = input().split()
    print(int(A) * int(B[0]+B[2:]) // 100)

if __name__ == '__main__':
    main()
