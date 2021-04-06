#!/usr/bin/env python3
import sys

def main():
    N, W = map(int, input().split())
    use = [0] * (2 * 10 ** 5 + 1)
    for _ in range(N):
        s, t, p = map(int, input().split())
        use[s] += p
        use[t] -= p
    t = 0
    for i in range(2 * 10 ** 5 + 1):
        t += use[i]
        if t > W:
            print("No")
            return
    print("Yes")
    return 

if __name__ == '__main__':
    main()
