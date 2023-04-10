#!/usr/bin/env python3
import sys


def main():
    H, W = map(int, input().split())
    F = []
    for _ in range(H):
        F.append(list(input()))
    for hh in range(H):
        s = F[hh]
        for ww in range(W - 1):
            if s[ww] == s[ww + 1] == "T":
                s[ww] = "P"
                s[ww + 1]= "C"
    for hh in range(H):
        print(*F[hh], sep="")

    return



if __name__ == '__main__':
    main()
