#!/usr/bin/env python3


def main():
    ans = 0
    H, W = map(int, input().split())
    l = []
    for _ in range(H):
        l.append(input())
    
    for h in range(H - 1):
        for w in range(W - 1):
            c = 0
            if l[h][w] == "#":
                c += 1
            if l[h][w + 1] == "#":
                c += 1
            if l[h + 1][w] == "#":
                c += 1
            if l[h + 1][w + 1] == "#":
                c += 1
            if c == 1 or c == 3:
                ans += 1
    print(ans)
if __name__ == '__main__':
    main()
