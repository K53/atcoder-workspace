#!/usr/bin/env python3

YES = "Yes"  # type: str
NO = "No"  # type: str


def main():
    N, M = map(int, input().split())
    B = []
    for _ in range(N):
        B.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(1, M):
            if B[i][j] - B[i][j - 1] != 1:
                print(NO)
                return

    for i in range(1, N):
        for j in range(M):
            if B[i][j] - B[i - 1][j] != 7:
                print(NO)
                return
    l = []
    for j in range(M):
        l.append((B[0][j] - 1) % 7)
    for j in range(1, M):
        if l[j] - l[j - 1] != 1:
            print(NO)
            return
    print(YES)
    return

    


if __name__ == '__main__':
    main()
