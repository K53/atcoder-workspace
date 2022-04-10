#!/usr/bin/env python3


def main():
    S = input()
    for i in range(3):
        a = set(S[i:(i + 3)])
        if len(a) == 1:
            print(*a)
            return
    print("draw")

if __name__ == '__main__':
    main()
