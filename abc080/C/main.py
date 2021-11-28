#!/usr/bin/env python3


def main():
    INF = 10 ** 16
    N = int(input())
    F = []
    P = []
    ans = -INF
    for _ in range(N):
        F.append(list(map(int, input().split())))
    for _ in range(N):
        P.append(list(map(int, input().split())))
    for i in range(1, 2 ** 10):
        sum = 0
        match = [0] * N
        for b in range(10):
            if i >> b & 1:
                for nn in range(N):
                    if F[nn][b] == 1:
                        match[nn] += 1
        for nn in range(N):
            sum += P[nn][match[nn]]
        ans = max(ans, sum)
    print(ans)                

if __name__ == '__main__':
    main()
