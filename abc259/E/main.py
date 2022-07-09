#!/usr/bin/env python3



from collections import defaultdict


def main():
    N = int(input())
    d = {} # 7: 2, set(2, 0)
    # print(d[0])
    f = 0
    for i in range(N):
        M = int(input())
        for mm in range(M):
            p, e = map(int, input().split())
            if p in d.keys():
                if d[p][0] < e:
                    d[p] = (e, i)
                    f = 1
                elif d[p][0] == e:
                    d[p] = (e, -1)
                else:
                    f = 1
                    continue
            else:
                d[p] = (e, i)
    # print(d)
    num = set()
    for _, idx in d.values():
        if idx == -1:
            f = 1
            continue
        num.add(idx)
    print(len(num) + f)








if __name__ == '__main__':
    main()
