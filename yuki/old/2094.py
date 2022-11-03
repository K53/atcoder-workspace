#!/usr/bin/env python3
INF = 10 ** 16
def main():
    N, K = map(int, input().split())
    black = 0
    for _ in range(2 * N):
        ss = input()
        black += ss.count("#")
    all = []
    fold = []
    for _ in range(2 * N):
        l = list(map(int, input().split()))
        all.extend(l)
        for i in range(N):
            fold.append(l[i] + l[-(i + 1)])
    all.sort(reverse=True)
    fold.sort(reverse=True)
    notsyn = sum(all[:black])
    if black % 2 == 1:
        print(notsyn)
    else:
        syn = sum(fold[:(black // 2)])
        print(max(notsyn, syn + K))

if __name__ == '__main__':
    main()