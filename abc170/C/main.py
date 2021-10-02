#!/usr/bin/env python3
import sys

def main():
    X, N = map(int, input().split())
    if N == 0:
        print(X)
        return
    pp = set(map(int, input().split())) ^ set(range(0, 102))
    m = 10 ** 9
    ans = -1
    for i in pp:
        if abs(i - X) < m:
            ans = i
            m = abs(i - X)
    print(ans)
    return
    



if __name__ == '__main__':
    main()
