#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        qq = list(map(int, input().split()))
        if qq[0] == 1:
            k, x = qq[1], qq[2]
            A[k - 1] = x
        else:
            k = qq[1]
            print(A[k - 1])
    return



if __name__ == '__main__':
    main()
