#!/usr/bin/env python3


def main():
    N = int(input())
    S = input()
    fS = list(S[:N])
    bS = list(S[N:])
    inv = False
    Q = int(input())
    for _ in range(Q):
        T, A, B = map(int, input().split())
        A -= 1
        B -= 1
        if T == 2:
            inv ^= True
        if T == 1:
            if not inv:
                if A < N and B < N:
                    fS[A], fS[B] = fS[B], fS[A]
                elif A >= N and B < N:
                    bS[A - N], fS[B] = fS[B], bS[A - N]
                elif A < N and B >= N:
                    fS[A], bS[B - N] = bS[B - N], fS[A]
                else:
                    bS[A - N], bS[B - N] = bS[B - N], bS[A - N]
            else:
                if A < N and B < N:
                    bS[A], bS[B] = bS[B], bS[A]
                elif A >= N and B < N:
                    fS[A - N], bS[B] = bS[B], fS[A - N]
                elif A < N and B >= N:
                    bS[A], fS[B - N] = fS[B - N], bS[A]
                else:
                    fS[A - N], fS[B - N] = fS[B - N], fS[A - N]
    if not inv:
        print("".join(fS + bS))
    else:
        print("".join(bS + fS))
    return



if __name__ == '__main__':
    main()
