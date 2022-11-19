#!/usr/bin/env python3
from collections import defaultdict

def main():
    H, W, N, hh, ww = map(int, input().split())
    # H, W, N, hh, ww = 300, 300, 300, 150, 150
    # A = [[i for i in range(W)] for _ in range(H)]
    A = [list(map(int, input().split())) for _ in range(H)]
    for st in range(H - hh + 1):
        d = defaultdict(int)
        for i in range(H):
            for j in range(W):
                if not (st <= i < st + hh and 0 <= j < ww):
                    d[A[i][j]] += 1
        # print(d)
        ini = len(d)
        # print(ini)
        count = ini
        ans = [ini]
        for j in range(1, W - ww + 1):
            for i in range(st, st + hh):
                # print(A[i][j - 1], A[i][ww - 1 + j], "now", count)
                if A[i][j - 1] == A[i][ww - 1 + j]:
                    continue
                if d[A[i][j - 1]] == 0:
                    # print(d[A[i][j - 1]], "%" )
                    count += 1
                d[A[i][j - 1]] += 1
                d[A[i][ww - 1 + j]] -= 1
                if d[A[i][ww - 1 + j]] == 0:
                    # print( d[A[i][ww - 1 + j]], "%!" )
                    count -= 1
                # print(count, "$")
                # print(d)
            # print(count)
            ans.append(count)
        print(*ans)
                    


        


            


if __name__ == '__main__':
    main()
