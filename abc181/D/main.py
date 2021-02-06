#!/usr/bin/env python3
import sys
from collections import Counter



# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    n = input()
    if len(n) <= 2:
        if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        exit()
    cnt = Counter(n)
    print(cnt)
    for i in range(112, 1000, 8):
        if not Counter(str(i)) - cnt:
            print(Counter(str(i)))
            print("Yes")
            exit()
    print("No")
if __name__ == '__main__':
    main()