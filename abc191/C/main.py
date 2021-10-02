#!/usr/bin/env python3


def main():
    ans = 0
    H, W = map(int, input().split())
    l = []
    for _ in range(H):
        l.append(input())
    
    for i in range(H - 1):
        for j in range(W - 1):
            block = 0
            for x in range(2):
                for y in range(2):
                    block += 1 if l[i + x][j + y] == "#" else 0
            if block == 1 or block == 3:
                ans += 1
    print(ans)    
    return

if __name__ == '__main__':
    main()
