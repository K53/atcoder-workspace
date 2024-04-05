#!/usr/bin/env python3


def main():
    Q = int(input())
    l = []
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            l.append(x)
        else:
            print(l[-x])

if __name__ == '__main__':
    main()
