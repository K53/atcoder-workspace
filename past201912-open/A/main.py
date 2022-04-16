#!/usr/bin/env python3
import sys

if __name__ == '__main__':
    S = input()
    if S[0].isdigit() and S[1].isdigit() and S[2].isdigit():
        print(int(S) * 2)
    else:
        print("error")