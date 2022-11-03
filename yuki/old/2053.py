#!/usr/bin/env python3
MOD = 998244353
def getArithmeticSequenceSum(a0: int, l: int, n: int):
    return (a0 + l) * n // 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    l = 1
    ans = 0
    for i in range(N - 1):
        d = A[i + 1] - A[i]
        if d == 1:
            l += 1
        else:
            ans += getArithmeticSequenceSum(1, l - 1, l - 1)
            l = 1
    ans += getArithmeticSequenceSum(1, l - 1, l - 1)
    print(ans)
    return

if __name__ == '__main__':
    main()