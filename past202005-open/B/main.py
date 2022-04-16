#!/usr/bin/env python3

def main():
    N, M, Q = map(int, input().split())
    points = [N] * M
    solved = [set() for _ in range(N)]
    for i in range(Q):
        l = list(map(int, input().split()))
        if l[0] == 1:
            ans = 0
            for ss in solved[l[1] - 1]:
                ans += points[ss]
            print(ans)
        else:
            points[l[2] - 1] -= 1
            solved[l[1] - 1].add(l[2] - 1)
    return


if __name__ == '__main__':
    main()
