#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    s1 = [0]
    s2 = [0]
    for i in range(N):
        s1.append(s1[i] + A[i])
    for i in range(1, N + 1):
        s2.append(s2[i - 1] + s1[i])
    maxs1 = max(s1)
    index = s1.index(maxs1)
    print(maxs1 + max(s2[index:]))
    
if __name__ == '__main__':
    main()
