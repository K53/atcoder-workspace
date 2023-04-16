#!/usr/bin/env python3

MOD = 998244353  # type: int
from collections import deque

def main():
    Q = int(input())
    d = deque([1])
    dig = 1
    ans = 1
    for _ in range(Q):
        t, *args = map(int, input().split())
        if t == 1:
            ans *= 10
            ans += args[0]
            ans %= MOD
            d.append(args[0])
            dig += 1
        elif t == 2:
            num = d.popleft()
            dig -= 1
            num *= pow(10, dig, MOD)
            num %= MOD
            ans -= num
            ans %= MOD
        else:
            print(ans)


if __name__ == '__main__':
    main()
