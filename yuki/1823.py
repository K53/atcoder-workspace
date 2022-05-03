#!/usr/bin/env python3
import sys

def main():
    T = int(input())
    for _ in range(T):
        X, Y = map(int, input().split())
        if X >= 5:
            print("Yes")
        else:
            if Y <= X:
                print("Yes")
            else:
                print("No")
    return


if __name__ == '__main__':
    main()
