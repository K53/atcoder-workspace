#!/usr/bin/env python3
import sys

def main():
    N = int(input())
    a = [input() for _ in range(N)]
    ans = []
    for i in range((N + 1) // 2):
        s = set(a[i]) & set(a[N - 1 - i])
        if len(s) == 0:
            print(-1)
            return
        ans.append(s.pop())
    if N % 2 == 0:
        print(*(ans + ans[::-1]), sep="")
    else:
        print(*(ans + ans[:-1][::-1]), sep="")
    return

if __name__ == '__main__':
    main()
