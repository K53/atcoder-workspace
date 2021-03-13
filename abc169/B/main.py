#!/usr/bin/env python3
import sys


def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    if A.count(0):
        print(0)
        return
    sum = 1
    for a in A:
        sum *= a
        if sum > 10 ** 18:
            print(-1)
            return
    print(sum)
    return


if __name__ == '__main__':
    main()
