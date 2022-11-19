#!/usr/bin/env python3
from collections import defaultdict

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N, Q = map(int, input().split())
    friends = defaultdict(set)
    for _ in range(Q):
        tt, aa, bb = map(int, input().split())
        if tt == 1:
            friends[aa].add(bb)
        if tt == 2 and bb in friends[aa]:
            friends[aa].remove(bb)
        if tt == 3:
            if bb in friends[aa] and aa in friends[bb]:
                print(YES)
            else:
                print(NO)
    return

if __name__ == '__main__':
    main()
