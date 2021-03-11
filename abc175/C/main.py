#!/usr/bin/env python3
import sys

def main():
    X, K, D =map(int, input().split())
    if X < 0:
        X *= -1
    p = X // D
    q = X % D
    rest = K - p
    if rest <= 0:
        ans = X - K * D
    else:
        ans = q if rest % 2 == 0 else abs(q - D)
    print(ans)


if __name__ == '__main__':
    main()
