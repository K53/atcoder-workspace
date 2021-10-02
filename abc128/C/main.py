#!/usr/bin/env python3

MOD = 2  # type: int

def main():
    ans = 0
    N, M = map(int, input().split())
    S = []
    for _ in range(M):
        l = list(map(lambda i : int(i) - 1, input().split()))
        S.append(l[1:])
    P = list(map(int, input().split()))

    ans = 0
    for state in range(2 ** N):
        for i in range(M):
            cnt = 0
            for b in S[i]:
                if state >> b & 1:
                    cnt += 1
            if cnt % 2 != P[i]:
                break
        else:
            ans += 1
    print(ans)
    return


if __name__ == '__main__':
    main()
