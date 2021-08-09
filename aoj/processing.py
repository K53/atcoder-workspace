#!/usr/bin/env python3
import sys

# まだ途中
# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_4_A&lang=ja

def main():
    N = int(sys.stdin.readline())
    lx = []
    ly = []
    m = []
    dx = dict()
    dy = dict()
    field = [[0 for _ in range(N * 2 + 1)] for _ in range(N * 2 + 1)]
    for _ in range(N):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        lx.append(x1)
        ly.append(y1)
        lx.append(x2)
        ly.append(y2)
        m.append((x1, y1, x2, y2))
    lx.sort()
    ly.sort()
    print(lx, ly)
    for i in range(2 * N):
        dx[lx[i]] = i
        dy[ly[i]] = i 
    for k, v in dx.items():
        print(k, v)
    print("#")
    for k, v in dy.items():
        print(k, v)
    for x1, y1, x2, y2 in m:
        field[dy[y1]][dx[x1]] += 1
        field[dy[y1]][dx[x2] + 1] -= 1
        field[dy[y2] + 1][dx[x1]] -= 1
        field[dy[y2] + 1][dx[x2] + 1] += 1
        for i in range(N * 2 + 1):
            print(field[i])
        print("###")


    
    for hh in range(N * 2 + 1):
        for ww in range(1, N * 2 + 1):
            field[hh][ww] += field[hh][ww - 1]
    for ww in range(N * 2 + 1):
        for hh in range(1, N * 2 + 1):
            field[hh][ww] += field[hh - 1][ww]
        
    for i in range(N * 2 + 1):
        print(field[i])

    return

if __name__ == '__main__':
    main()
