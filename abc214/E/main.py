#!/usr/bin/env python3
NO = "No"  # type: str
YES = "Yes"  # type: str

import heapq
import bisect
from collections import defaultdict
def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        d = defaultdict(list)
        ls = []
        for _ in range(N):
            ll, rr = map(int, input().split())
            ls.append(ll)
            d[ll].append(rr)
        ls.sort()
        # print(ls)
        q = []
        now = 1
        done = 0
        while True:
            if done == N:
                print(YES)
                break
            for rr in d[now]:
                heapq.heappush(q, rr)
            if len(q) == 0:
                # print(now)
                # print(ls[bisect.bisect_right(ls, now)])
                # print("#", now)
                now = ls[bisect.bisect_right(ls, now)]
                continue
            rr = heapq.heappop(q)
            done += 1
            if now > rr:
                print(NO)
                break
            now += 1
        



if __name__ == '__main__':
    main()
