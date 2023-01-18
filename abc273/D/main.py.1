#!/usr/bin/env python3


from bisect import bisect_right, bisect_left
from collections import defaultdict


def main():
    H, W, now_y, now_x = map(int, input().split())
    N = int(input())
    d_yoko = defaultdict(lambda : [0])
    d_tate = defaultdict(lambda : [0])
    qs = []
    for _ in range(N):
        r, c = map(int, input().split())
        qs.append((r, c))
    qs.sort()
    for r, c in qs:
        d_yoko[r].append(c)
        d_tate[c].append(r)
    for d in d_yoko.values():
        d.append(W + 1)
    for d in d_tate.values():
        d.append(H + 1)
    Q = int(input())
    for _ in range(Q):
        dl = input().split()
        d, l = dl[0], int(dl[1])
        if d == "L":
            idx = bisect_left(d_yoko[now_y], now_x) 
            if d_yoko[now_y][idx - 1] < now_x - l:
                now_x = now_x - l
            else:
                now_x = d_yoko[now_y][idx - 1] + 1

            print(now_y, now_x)
        elif d == "R":
            idx = bisect_left(d_yoko[now_y], now_x) 
            print(d_yoko[now_y], idx)
            if d_yoko[now_y][idx] > now_x + l:
                now_x = now_x + l
            else:
                now_x = d_yoko[now_y][idx] - 1


            print(now_y, now_x)
        elif d == "U":
            idx = bisect_left(d_tate[now_x], now_y) 
            if d_tate[now_x][idx - 1] < now_y - l:
                now_y = now_y - l
            else:
                now_y = d_tate[now_x][idx - 1] + 1

            print(now_y, now_x)
        else:
            idx = bisect_left(d_tate[now_x], now_y)
            if d_tate[now_x][idx] > now_y + l:
                now_y = now_y + l
            else:
                now_y = d_tate[now_x][idx] - 1

            print(now_y, now_x)

            
                

            


if __name__ == '__main__':
    main()
