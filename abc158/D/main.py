#!/usr/bin/env python3
from collections import deque

def main():
    S = input()
    ans = deque()
    for s in S:
        ans.append(s)
    Q = int(input())
    reverse = False
    for _ in range(Q):
        l = input().split()
        if l[0] == "1":
            reverse = not reverse
        else:
            if (l[1] == "1" and not reverse) or (l[1] == "2" and reverse):
                ans.appendleft(l[2])
            else:
                ans.append(l[2])
    ans = list(ans)
    if reverse:
        print(*ans[::-1], sep="")
    else:
        print(*ans, sep="")

if __name__ == '__main__':
    main()
