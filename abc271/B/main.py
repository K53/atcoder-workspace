#!/usr/bin/env python3

def main():
    N, Q = map(int, input().split())
    l = []
    for _ in range(N):
        l.append(list(map(int, input().split()))[1:])
    for _ in range(Q):
        s, t = map(int, input().split())
        print(l[s - 1][t - 1])
    return

if __name__ == '__main__':
    main()
