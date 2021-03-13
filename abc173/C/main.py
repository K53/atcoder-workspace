#!/usr/bin/env python3


def main():
    H, W, K = map(int, input().split())
    grid = []
    for _ in range(H):
        grid.append(list(map(lambda i : 0 if i == "." else 1, list(input()))))

    ans = 0
    for i in range(2 ** H):
        for j in range(2 ** W):
            count = 0
            for h in range(H):
                for w in range(W):
                    if i >> h & 1:
                        continue
                    if j >> w & 1 :
                        continue
                    count += grid[h][w]
            if count == K:
                ans += 1
    print(ans)


if __name__ == '__main__':
    main()
