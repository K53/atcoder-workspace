#!/usr/bin/env python3
INF = 10 ** 9

def main():
    N, M, X = map(int, input().split())
    C, A = [], []
    for _ in range(N):
        CA = list(map(int, input().split()))
        C.append(CA[0])
        A.append(CA[1:])
    ans = INF
    for n in range(2 ** N):
        skill = [0] * M
        cost = 0
        for i in range(N):
            if n >> i & 1 == 1:
                skill = [x + y for (x, y) in zip(skill, A[i])]
                cost += C[i]
        for j in range(M):
            if skill[j] < X:
                break
        else:
            ans = min(ans, cost)
    print(-1 if ans == INF else ans)



if __name__ == '__main__':
    main()
