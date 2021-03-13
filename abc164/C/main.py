#!/usr/bin/env python3
import sys


def main():
    s = set()
    N = int(input())
    for _ in range(N):
        s.add(input())
    print(len(list(s)))


if __name__ == '__main__':
    main()
