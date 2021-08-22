#!/usr/bin/env python3
import sys

YES = "YES"  # type: str
NO = "NO"  # type: str


def main():
    sys.setrecursionlimit(10 ** 9)
    import copy
    H, W = 10, 10
    field = []
    for _ in range(H):
        field.append(list(input()))
    def dfs(y, x, f):
        f[y][x] = "x"
        # 次の探索(分岐)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_y = y + dy
            next_x = x + dx
            # 探索しない条件を切り落とし
            if next_x < 0 or next_y < 0 or next_x >= W or next_y >= H or f[next_y][next_x] == "x":
                continue
            dfs(next_y, next_x, f)
        return
    for hh in range(H):
        for ww in range(W):
            if field[hh][ww] == "o":
                continue
            f = copy.deepcopy(field)
            f[hh][ww] = "o"
            count = 0
            for sh in range(H):
                for sw in range(W):
                    if f[sh][sw] == "x":
                        continue
                    dfs(sh, sw, f)
                    count += 1
            if count == 1:
                print(YES)
                return
    print(NO)
    return


if __name__ == '__main__':
    main()
