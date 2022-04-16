#!/usr/bin/env python3

from copy import deepcopy


if __name__ == '__main__':
    N, Q = map(int, input().split())
    follow = [set() for _ in range(N)]
    follower = [set() for _ in range(N)]
    for _ in range(Q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            follow[l[1] - 1].add(l[2] - 1)
            follower[l[2] - 1].add(l[1] - 1)
        elif l[0] == 2:
            for f in follower[l[1] - 1]:
                follow[l[1] - 1].add(f)
                follower[f].add(l[1] - 1)
        else:
            for x in deepcopy(follow[l[1] - 1]):
                for f in follow[x]:
                    if f != l[1] - 1:
                        follow[l[1] - 1].add(f)
                        follower[f].add(l[1] - 1)
    
    ans = [["N" for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for f in follow[i]:
            ans[i][f] = "Y"
    
    for i in range(N):
        print(*ans[i], sep="")
    