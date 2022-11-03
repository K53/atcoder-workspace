#!/usr/bin/env python3
MOD = 998244353
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += A[i] * (pow(2, N - 1 - i, MOD) - 1) - A[i] * (pow(2, i, MOD) - 1)
    print(ans % MOD)
    return

if __name__ == '__main__':
    main()