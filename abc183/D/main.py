#!/usr/bin/env python3
import sys

def main():
    N, W = map(int, input().split())
    l = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        l.append((s, p))    # 使用開始時に加算
        l.append((t, -p))   # 使用終了時に減算
    l.sort()
    using = 0
    for time, delta in l:
        using += delta
        if using > W:
            print("No")
            return
    print("Yes")
    return    

if __name__ == '__main__':
    main()
