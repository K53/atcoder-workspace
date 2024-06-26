#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    S = input()
    Q = int(input())
    queries = [list(input().split()) for _ in range(Q)][::-1]
    ans = ["_"] * N
    flag = 0

    for qq in queries:
        if qq[0] == "1" and ans[int(qq[1]) - 1] == "_":
            if flag == 0:
                ans[int(qq[1]) - 1] = qq[2]
            elif flag == 2:
                ans[int(qq[1]) - 1] = qq[2].lower()
            else:
                ans[int(qq[1]) - 1] = qq[2].upper()
        if flag != 0:
            continue
        if qq[0] == "2":
            flag = 2
        if qq[0] == "3":
            flag = 3

    for i in range(N):
        if ans[i] != "_":
            continue
        if flag == 0:
            ans[i] = S[i]
        if flag == 2:
            ans[i] = S[i].lower()
        if flag == 3:
            ans[i] = S[i].upper()

    print(*ans, sep="")


if __name__ == '__main__':
    main()
