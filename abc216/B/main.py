#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


# Generated by 2.8.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = input().split()
        S.append(s)
        T.append(t)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if S[i] == S[j] and T[i] == T[j]:
                print(YES)
                return
    print(NO)
    return

if __name__ == '__main__':
    main()
