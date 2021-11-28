#!/usr/bin/env python3


def main():
    N = int(input())
    d = set()
    for _ in range(N):
        l = tuple(map(int, input().split()))
        d.add(l[1:])
    print(len(d))
    return

if __name__ == '__main__':
    main()
