#!/usr/bin/env python3

def main():
    N = int(input())
    C = list(input())
    r = N
    ans = 0
    for l in range(N):
        if C[l] == "W":
            for _ in range(N):
                r -= 1
                # print(l, r)
                # print(C)
                if l >= r:
                    print(ans)
                    return
                if C[r] == "R":
                    C[l], C[r] = C[r], C[l]
                    ans += 1
                    break
    print(ans)

if __name__ == '__main__':
    main()
