#!/usr/bin/env python3
import sys

# https://atcoder.jp/contests/joi2012ho/tasks/joi2012ho4

def main():
    field = [[0 for _ in range(5000 + 1 + 2)] for _ in range(5000 + 1 + 2)]
    N, M = map(int, sys.stdin.readline().split())
    for i in range(M):
        a, b, x = map(int, sys.stdin.readline().split())
        field[a][b] += 1
        field[a][b + 1] -= 1
        field[a + x + 1][b] -= 1
        field[a + x + 2][b + 1] += 1
        field[a + x + 1][b + x + 2] += 1
        field[a + x + 2][b + x + 2] -= 1
    
    for hh in range(5000 + 1 + 2):
        for ww in range(1, 5000 + 1 + 2):
            field[hh][ww] += field[hh][ww - 1]

    for ww in range(5000 + 1 + 2):
        for hh in range(1, 5000 + 1 + 2):
            field[hh][ww] += field[hh - 1][ww]

    for hh in range(1, 5000 + 1 + 2):
        for ww in range(1, 5000 + 1 + 2):
            field[hh][ww] += field[hh - 1][ww - 1]
    
    ans = 0
    for hh in range(5000 + 1 + 2):
        for ww in range(5000 + 1 + 2):
            if field[hh][ww] > 0:
                ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
