#!/usr/bin/env python3


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        c = 0
        l = map(int, input().split())
        for ll in l:
            if int(str(ll)[-1]) % 2 == 1:
                c += 1
        print(c)
    return

if __name__ == '__main__':
    main()
