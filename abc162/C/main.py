#!/usr/bin/env python3
import sys
import math

def main():
    K = int(input())
    ans = 0
    for a in range(1, K + 1):
        for b in range(a, K + 1):
            for c in range(b, K + 1):
                if a == b == c:
                    comb = 1
                elif a == b or b == c or c == a:
                    comb = 3
                else:
                    comb = 6
                ans += math.gcd(math.gcd(a,b),c) * comb
    print(ans)
if __name__ == '__main__':
    main()
