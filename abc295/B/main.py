#!/usr/bin/env python3


def main():
    H, W = map(int, input().split())
    G = []
    bomb = []
    for hh in range(H):
        ll = list(input())
        for ww in range(W):
            if ll[ww] != "." and ll[ww] != "#":
                bomb.append((hh, ww, ll[ww]))
        G.append(ll)
    # print(bomb)
    for hh, ww, bb in bomb:
        bb = int(bb)
        for dy in range(-bb, bb + 1):
            for dx in range(-bb, bb + 1):
                nexth = hh + dy
                nextw = ww + dx 
                # print(bb, nexth, nextw)
                if abs(dy) + abs(dx) <= bb and 0 <= nexth < H and 0 <= nextw < W:
                    # print("ok", nexth, nextw)
                    G[nexth][nextw] = "."
    for hh in range(H):
        print(*G[hh], sep="")



        
    
    
    

if __name__ == '__main__':
    main()
