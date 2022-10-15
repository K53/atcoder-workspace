#!/usr/bin/env python3


from bisect import bisect_right, bisect_left
from collections import defaultdict


def main():
    H, W, now_y, now_x = map(int, input().split())
    N = int(input())
    d_yoko = defaultdict(list)
    d_tate = defaultdict(list)
    qs = []
    for _ in range(N):
        r, c = map(int, input().split())
        qs.append((r, c))
    qs.sort()
    for r, c in qs:
        d_yoko[r].append(c)
        d_tate[c].append(r)
    Q = int(input())
    for _ in range(Q):
        dl = input().split()
        d, l = dl[0], int(dl[1])
        if d == "L":
            # print(d_yoko[now_y])
            idx = bisect_left(d_yoko[now_y], now_x) 
            # print(idx)
            if idx == 0:
                now_x = now_x - l
            else:
                if d_yoko[now_y][idx - 1] < now_x - l:
                    now_x = now_x - l
                else:
                    now_x = d_yoko[now_y][idx - 1] + 1
            if now_x <= 0:
                now_x = 1
            elif now_x >= W + 1:
                now_x = W

            print(now_y, now_x)
        elif d == "R":
            # print(d_yoko[now_y], now_x)
            idx = bisect_left(d_yoko[now_y], now_x) 
            if idx == len(d_yoko[now_y]):
                now_x = now_x + l
            else:
                if d_yoko[now_y][idx] > now_x + l:
                    # print("")
                    now_x = now_x + l
                else:
                    # print("a",d_yoko[now_y][idx], now_x + l)
                    # print(d_yoko[now_y][idx - 1])
                    now_x = d_yoko[now_y][idx - 1] - 1
            if now_x <= 0:
                now_x = 1
            elif now_x >= W + 1:
                now_x = W

            print(now_y, now_x)
        elif d == "U":
            # print(d_yoko[now_y])
            idx = bisect_left(d_tate[now_x], now_y) 
            # print(idx)
            if idx == 0:
                now_y = now_y - l
            else:
                if d_tate[now_x][idx - 1] < now_y - l:
                    now_y = now_y - l
                else:
                    now_y = d_tate[now_x][idx - 1] + 1
            if now_y <= 0:
                now_y = 1
            elif now_y >= H + 1:
                now_y = H

            print(now_y, now_x)
        else:
            idx = bisect_left(d_tate[now_x], now_y) 
            if idx == len(d_tate[now_x]):
                now_y = now_y + l
            else:
                if d_tate[now_x][idx] > now_y + l:
                    now_y = now_y + l
                else:
                    now_y = d_tate[now_x][idx - 1] - 1
            if now_y <= 0:
                now_y = 1
            elif now_y >= H + 1:
                now_y = H
                
            print(now_y, now_x)

            
                

            


if __name__ == '__main__':
    main()
