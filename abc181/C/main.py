#!/usr/bin/env python3
import sys
import itertools

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N = int(input())
    nodes = []
    for _ in range(N):
        x, y = map(int, input().split())
        nodes.append((x, y))
    pairs = list(itertools.combinations(nodes, 3))
    for p in pairs:
        if p[0][0] == p[1][0] == p[2][0]:
            print(YES)
            return
        if (p[1][1] - p[0][1]) * (p[1][0] - p[2][0]) == (p[1][1] - p[2][1]) * (p[1][0] - p[0][0]):
            print(YES)
            return
    print(NO)
    return
            
if __name__ == '__main__':
    main()
