#!/usr/bin/env python3
import math

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    A = list(map(int, input().split()))
    A.extend([0, N + 1])
    A.sort()
    diff = []
    for i in range(len(A) - 1):
        diff.append(A[i + 1] - A[i] - 1)
    diff.sort()
    m = 0
    ans = 0
    for d in diff:
        if d == 0:
            continue
        if m == 0:
            m = d
        ans += math.ceil(d / m)
    print(ans)
        
    

if __name__ == '__main__':
    main()
