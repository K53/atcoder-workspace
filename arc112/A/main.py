#!/usr/bin/env python3


def main():
    T = int(input())
    for _ in range(T):
        L, R = map(int, input().split())
        K = R - 2 * L + 1
        if K < 0:
            print(0)
        else:
            print(K * (K + 1) // 2)

if __name__ == '__main__':
    main()
