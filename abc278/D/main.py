#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    offset = 0
    ok = set(range(N))
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            offset = x
            # A = [0] * N
            ok = set()
        elif query[0] == 2:
            i = query[1] - 1
            x = query[2]
            if i in ok:
                A[i] += x
            else:
                A[i] = x
                ok.add(i)
        else:
            i = query[1] - 1
            if i in ok:
                print(offset + A[i])
            else:
                print(offset)
    return


if __name__ == '__main__':
    main()
