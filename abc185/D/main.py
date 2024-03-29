#!/usr/bin/env python3


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    N, M = map(int, input().split())
    if M == 0:
        print(1)
        return
    A = sorted(list(map(lambda x: int(x) - 1, input().split())))
    if A[0] != -1:
        A = [-1] + A
    if A[-1] != N - 1:
        A.append(N)

    wid = N
    # print(A)
    for i in range(len(A) - 1):
        if A[i + 1] - A[i] - 1 == 0:
            continue
        wid = min(wid, A[i + 1] - A[i] - 1)
    # print(wid)
    ans = 0
    for i in range(len(A) - 1):
        dist = A[i + 1] - A[i] - 1
        if dist == 0:
            continue
        # print(dist)
        p, q = divmod(dist, wid)
        if q != 0:
            p += 1
        ans += p
    print(ans)        
    return

if __name__ == '__main__':
    main()
