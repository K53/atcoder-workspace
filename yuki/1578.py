#!/usr/bin/env python3
def main():
    MOD = 10 ** 9 + 7
    A, B, C = map(int, input().split())
    K = int(input())
    r = pow(2, K, MOD - 1)
    print(pow((A * B * C) % MOD, r, MOD))

if __name__ == '__main__':
    main()