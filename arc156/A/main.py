#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    T = int(input())
    # T = 50
    for i in range(T):
        N = int(input())
        S = input()
        # S = bin(i)[2:]
        # print(S)
        aa = S.count("1")
        if aa % 2 == 1:
            print(-1)
        else:
            if aa == 2 and "11" in S:
                if S == "011" or S == "110" or S == "11":
                    print(-1)
                elif S == "0110":
                    print(3)
                else:
                    print(2)
            else:
                print(aa // 2)
                
                

if __name__ == '__main__':
    main()
