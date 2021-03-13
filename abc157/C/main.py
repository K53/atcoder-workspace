#!/usr/bin/env python3
import sys


def main():
    N, M = map(int, input().split())
    ans = [-1] * N
    for _ in range(M):
        s, c = map(int, input().split())
        if ans[s - 1] == -1 or ans[s - 1] == c:
            ans[s - 1] = c
        else:
            print(-1)
            return
    for i in range(N):
        if ans[i] == -1:
            if N != 1 and i == 0:
                ans[i] = 1
            else:
                ans[i] = 0
    if N != 1 and ans[0] == 0:
        print(-1)
    else:
        print(*ans, sep="")
    return


            


if __name__ == '__main__':
    main()
