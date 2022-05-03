#!/usr/bin/env python3
import sys

def main():
    ans = 0
    N = int(input())
    for i in range(1, 10 ** 5 + 1):
        if int(str(i) * 3) <= N:
            ans += 1
    print(ans)
    return


if __name__ == '__main__':
    main()