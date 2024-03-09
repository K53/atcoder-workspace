#!/usr/bin/env python3

INF = 10 ** 12
def main():
    T = input()
    N = int(input())
    bags = []
    baglens = []
    for _ in range(N):
        l = input().split()
        baglens.append(int(l[0]))
        bags.append(l[1:])
    # print(baglens)
    # print(bags)

    dp = [[INF] * (len(T) + 1) for _ in range(N + 1)]
    dp[0][0] = 0

    for i in range(N):
        for tt in range(len(T) + 1): # tt桁目のT[tt]はまだ
            if dp[i][tt] == INF:
                continue
            for ssak in bags[i]:  # ['ab', 'abc', 'abcd']
                # print(i, tt ,ssak, T[tt:(tt + len(ssak))])
                if T[tt:(tt + len(ssak))] == ssak and tt + len(ssak) < len(T) + 1:
                    dp[i + 1][tt + len(ssak)] = min(dp[i + 1][tt + len(ssak)], dp[i][tt] + 1)
            dp[i + 1][tt] = min(dp[i + 1][tt], dp[i][tt])
    
    # print(*dp,sep="\n")
    print(-1 if dp[-1][-1] == INF else dp[-1][-1])

if __name__ == '__main__':
    main()
