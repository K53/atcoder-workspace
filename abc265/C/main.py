#!/usr/bin/env python3


from posixpath import split


def main():
    H, W = map(int, input().split())
    G = []
    for _ in range(H):
        G.append(input())
    # print(G)   # ['.....', '.###.', '.###.', '.###.', '.....']
    nowx, nowy = 0, 0
    for _ in range(H * W):
        dir = G[nowy][nowx]
        # print(dir)
        if dir == "U":
            if nowy != 0:
                nowy -= 1
            else:
                print(nowy + 1, nowx + 1)
                return
        elif dir == "D":
            if nowy != H - 1:
                nowy += 1
            else:
                print(nowy + 1, nowx + 1)
                return
        elif dir == "L":
            if nowx != 0:
                nowx -= 1
            else:
                print(nowy + 1, nowx + 1)
                return
        else: #if dir == "R":
            if nowx != W - 1:
                nowx += 1
            else:
                print(nowy + 1, nowx + 1)
                return
        # print(nowx, nowy, "#")
    print(-1)
    return

if __name__ == '__main__':
    main()
