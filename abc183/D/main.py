#!/usr/bin/env python3
import sys

def main():
    N, W = map(int, input().split())

    # テーブルの初期化
    imos = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        ss, tt, pp = map(int, input().split())
        imos[ss] += pp
        imos[tt] -= pp

    # ビルド
    for i in range(1, len(imos)):
        imos[i] += imos[i - 1]
    
    for m in imos:
        if m > W:
            print("No")
            return
    # print(imos)
    print("Yes")
    return 

if __name__ == '__main__':
    main()
