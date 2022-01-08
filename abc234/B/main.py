#!/usr/bin/env python3


def main():
    N = int(input())
    l = []
    for _ in range(N):
        x, y = map(int, input().split())
        l.append((x, y))
    ans = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            ans = max(ans, (abs(l[i][0] - l[j][0]) ** 2 + abs(l[i][1] - l[j][1]) ** 2) ** (1/2))
    print(ans)


if __name__ == '__main__':
    main()
