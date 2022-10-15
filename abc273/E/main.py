#!/usr/bin/env python3
from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

def main():
    Q = int(input())
    notesL = set()
    qs = []
    for _ in range(Q):
        qq = input()[:-1].split(" ")
        # print(qq)
        if qq[0] == "DELETE":
            qs.append((qq[0], 0))
        else:
            qs.append((qq[0], int(qq[1])))
            if qq[0] != "ADD":
                notesL.add(qq[1])
    # print(qs)
    # print(notesL)
    l = sorted(list(notesL))
    d = dict()
    for i, num in enumerate(notesL):
        # print(i + 1, num)
        d[num] = i
    
    notes = [None for _ in range(len(notesL))]
    A = deque()
    ans = []
    for query in qs:
        # print(query)
        num = int(query[1])
        if query[0] == "ADD":
            A.append(num)
        elif query[0] == "DELETE":
            if len(A) > 0:
                A.pop()
        elif query[0] == "SAVE":
            notes[d[str(num)]] = deepcopy(A)
        else:
            A = notes[d[str(num)]]
            if A == None:
                A = deque()
        ans.append(A[-1] if len(A) > 0 else -1)


    print(*ans, sep=" ")


if __name__ == '__main__':
    main()
