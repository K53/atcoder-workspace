#!/usr/bin/env python3
import sys


def solve(N: int, P: int, S: str):
    if P == 2 or P == 5:
        ans = 0
        for i in range(N):
            if int(S[i]) % P == 0:
                ans += i + 1
        print(ans)
        return
    num = [0] * P
    invS = S[::-1]
    d = 1
    now = 0
    for i in range(N):
        now = (int(invS[i]) * d + now) % P
        num[now] += 1
        d = d * 10 % P
    ans = num[0]
    for i in num:
        ans += i * (i - 1) // 2
    print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    P = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, P, S)

if __name__ == '__main__':
    main()
