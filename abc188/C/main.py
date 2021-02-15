#!/usr/bin/env python3


def main():
    N = int(input())
    A = list(map(int, input().split()))

    win = A
    lose = []
    while len(win) != 1:
        w, l = [], []
        for i in range(0, len(win), 2):
            w.append(max(win[i], win[i + 1]))
            l.append(min(win[i], win[i + 1]))
        win, lose = w, l
    print(A.index(lose[0]) + 1)
    return

if __name__ == '__main__':
    main()
