#!/usr/bin/env python3


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    s = input()
    if len(set(s)) == 1:
        print("Weak")
        return
    if (int(s[0]) + 1) % 10 == int(s[1]) and (int(s[1]) + 1) % 10 == int(s[2]) and (int(s[2]) + 1) % 10 == int(s[3]):
        print("Weak")
        return
    print("Strong")
    return
    

if __name__ == '__main__':
    main()