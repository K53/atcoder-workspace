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
    
    for n in range(2 ** N):
        onSwitch = [0] * M
        for i in range(N):
            if (n >> i) & 1:
                for m in range(M):
                    if i in S[m]:
                        onSwitch[m] += 1
        for m in range(M):
            if onSwitch[m] % 2 != P[m]:
                break
        else:
            ans += 1
    print(ans)





    


if __name__ == '__main__':
    main()
