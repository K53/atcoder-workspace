#!/usr/bin/env python3


def main():
    H, W, K = map(int, input().split())
    c = []
    tot = 0
    for _ in range(H):
        l = input()
        c.append(l)
        tot += l.count("#")
    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            s = set()
            for b in range(H):
                for t in range(W):
                    if ((i >> b) & 1 or (j >> t) & 1) and c[b][t] == "#":
                        s.add((b, t))
            if tot - len(s) == K:
                ans += 1
    print(ans)
    return
                        
                        


if __name__ == '__main__':
    main()
