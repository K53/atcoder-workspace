#!/usr/bin/env python3
import string

def main():
    l = string.ascii_lowercase
    invl = (string.ascii_lowercase)[::-1]
    N = int(input())
    S = input()
    ans = []
    for ss in S:
        ans.append(invl[l.index(ss)])
    print(*ans, sep="")
    return

if __name__ == '__main__':
    main()