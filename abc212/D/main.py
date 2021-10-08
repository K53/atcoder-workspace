#!/usr/bin/env python3


def main():
    import heapq
    Q = int(input())
    h = []
    now = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(h, query[1] - now)
        elif query[0] == 2:
            now += query[1]
        else:
            print(heapq.heappop(h) + now)
    return



if __name__ == '__main__':
    main()
