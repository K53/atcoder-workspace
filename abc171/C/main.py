#!/usr/bin/env python3
import sys
import string

S = string.ascii_lowercase

def convert(q):
    return S[q - 1]
    
def main():
    N = int(input())
    ans = []
    while N != 0:
        N, q = divmod(N, 26)
        ans.append(convert(q))
        if q == 0:
            N -= 1
    print("".join(ans[::-1]))
    return
    




if __name__ == '__main__':
    main()
