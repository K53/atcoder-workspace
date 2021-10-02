#!/usr/bin/env python3


def main():
    N = int(input())
    A = []
    for _ in range(N):
        a = int(input())
        XYs = []
        for _ in range(a):
            x, y = map(int, input().split())
            XYs.append((x - 1, y))
        A.append(XYs)
    # print(A)

    ans = 0
    for case in range(2 ** N):
        flg = True
        for i in range(N):
            if case >> i & 1:
                for num in A[i]:
                    if (case >> num[0] & 1) != num[1]:
                        flg = False
        if flg:
            c = 0
            for i in range(N):
                if case >> i & 1:
                    c += 1
            ans = max(ans, c)
    print(ans)
    return


if __name__ == '__main__':
    main()
