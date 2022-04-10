#!/usr/bin/env python3


def main():
    N = int(input())
    Q = int(input())
    x = [i for i in range(N)]
    y = [i for i in range(N)]
    inv = 0
    for _ in range(Q):
        query = list(map(int, input().split()))
        if (inv == 0 and query[0] == 1) or (inv == 1 and query[0] == 2):
            A, B = query[1], query[2]
            y[A - 1], y[B - 1] = y[B - 1], y[A - 1]
        elif (inv == 0 and query[0] == 2) or (inv == 1 and query[0] == 1):
            A, B = query[1], query[2]
            x[A - 1], x[B - 1] = x[B - 1], x[A - 1]
        elif query[0] == 3:
            inv ^= 1
        else:
            A, B = query[1], query[2]
            if inv:
                A, B = B, A
            originalY, originalX = y[A - 1], x[B - 1]
            # print(originalY, originalX)
            print(N * originalY + originalX)
    return


if __name__ == '__main__':
    main()
