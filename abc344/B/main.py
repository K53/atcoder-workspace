#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    ans = []
    while True:
        num = int(input()) 
        ans.append(num)
        if num == 0:
            break
    print(*ans[::-1], sep="\n")

if __name__ == '__main__':
    main()
