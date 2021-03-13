#!/usr/bin/env python3
import sys
import string

def getpq(n: int):
    p = n // 26
    q = n % 26
    return (p, q)

def main():
    N = int(input())
    S = string.ascii_lowercase
    p = N - 1
    ans = ""
    while True:
        p, q = getpq(p)
        ans = S[q] + ans
        # print(p, q)
        if p == 0:
            break
        p -= 1

    print(ans)


if __name__ == '__main__':
    main()
