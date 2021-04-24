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
        if T == 2:
            inv ^= True
        if T == 1:
            aa, bb = "", ""
            ia, ib = 0, 0
            if not inv:
                if A > N and B > N:
                    bS[A - N - 1], bS[B - N - 1] = bS[B - N - 1], bS[A - N - 1]
                elif A > N and B <= N:
                    bS[A - N - 1], fS[B - 1] = fS[B - 1], bS[A - N - 1]
                elif A <= N and B > N:
                    fS[A - 1], bS[B - N - 1] = bS[B - N - 1], fS[A - 1]
                else:
                    fS[A - 1], fS[B - 1] = fS[B - 1], fS[A - 1]
            else:
                if A > N and B > N:
                    fS[A - N - 1], fS[B - N - 1] = fS[B - N - 1], fS[A - N - 1]
                elif A > N and B <= N:
                    fS[A - N - 1], bS[B - 1] = bS[B - 1], fS[A - N - 1]
                elif A <= N and B > N:
                    bS[A - 1], fS[B - N - 1] = fS[B - N - 1], bS[A - 1]
                else:
                    bS[A - 1], bS[B - 1] = bS[B - 1], bS[A - 1]
    if inv:
        print(*(bS + fS), sep="")
    else:
        print(*(fS + bS), sep="")           
    return
                



if __name__ == '__main__':
    main()
