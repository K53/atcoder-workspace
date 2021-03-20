#!/usr/bin/env python3
import sys



def main():
    x = input()
    if "." in x:
        s = x.split(".")
        print(s[0])
    else:
        print(x)

if __name__ == '__main__':
    main()
