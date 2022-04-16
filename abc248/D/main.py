#!/usr/bin/env python3

import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    nums = [[] for _ in range(N + 1)] 
    for i in range(N):
        nums[A[i]].append(i)
    # print(nums)
    Q = int(input())
    for i in range(Q):
        s, t, v = map(int, input().split())
        ss = bisect.bisect_left(nums[v], s - 1)
        tt = bisect.bisect_left(nums[v], t - 1)
        print(tt - ss)
            

    return



if __name__ == '__main__':
    main()
