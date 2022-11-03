#!/usr/bin/env python3
def main():
    T = int(input())
    X, A = map(int, input().split())
    Y, B = map(int, input().split())
    # p * X + q + r * Y
    ans = 10 ** 15
    for r in range(10 ** 7 + 1):
        dist = T + r * B
        if dist < 0:
            continue
        p, q = dist // A, dist % A
        ans = min(ans, p * X + q + r * Y)
    print(ans)
    return

if __name__ == '__main__':
    main()