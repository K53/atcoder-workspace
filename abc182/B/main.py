#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    maxCount = 0
    ans = 1
    for i in range(2, 1001):
        count = 0
        for a in A:
            if a % i == 0:
                count += 1
        if count > maxCount:
            maxCount = count
            ans = i
    print(ans)
    return

if __name__ == '__main__':
    main()
