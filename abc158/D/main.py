#!/usr/bin/env python3
from collections import deque

def main():
    S = input()
    Q = int(input())
    ans = deque(S)
    inv = False
    for _ in range(Q):
        query = input().split()
        if query[0] == "1":
            inv ^= True
        else:
            if query[1] == "1":
                if inv:
                    ans.append(query[2])
                else:
                    ans.appendleft(query[2])
            else:
                if inv:
                    ans.appendleft(query[2])
                else:
                    ans.append(query[2])
    if not inv:
        print(*ans, sep="")
    else:
        print(*(list(ans)[::-1]), sep="")
    return

if __name__ == '__main__':
    main()
