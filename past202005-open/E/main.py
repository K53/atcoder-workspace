#!/usr/bin/env python3

def main():
    N, M, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    c = list(map(int, input().split()))
    for _ in range(Q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            p = l[1] - 1
            print(c[p])
            for next in G[p]:
                c[next] = c[p]
        else:
            p = l[1] - 1
            print(c[p])
            c[p] = l[2]
    return

if __name__ == '__main__':
    main()
