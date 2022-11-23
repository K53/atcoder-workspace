#!/usr/bin/env python3
from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxA = max(A)
    d = Counter(A)
    M = 10 ** 5
    used = False

    recov = maxA
    for k, v in d.items():
        if v >= 3:
            recov = k
            break

    for i in range(M):
        if d[i] >= 2:
            continue
        elif d[i] == 1:
            if recov != -1 and recov != i:
                d[recov] -= 1
                d[i] += 1
                recov = -1
                continue
            else:
                seq = i
                break
        else:
            seq = i
            break
            
    print(seq)
    return

if __name__ == '__main__':
    main()