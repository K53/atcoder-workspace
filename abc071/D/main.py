#!/usr/bin/env python3
import sys

MOD = 1000000007  # type: int


def solve(N: int, S: "List[str]"):
    A = S[0]
    B = S[1]
    ans = 1
    i = 0
    while i < len(A):#N:
        # print(i, A[i], B[i], ans)
        if i == 0:
            if A[i] != B[i]:  # 横
                ans *= 3 * 2
                i += 1
            else: # 縦
                ans *= 3
        elif A[i - 1] == B[i - 1]:
            if A[i] != B[i]:  # 縦 - 横
                ans *= 2
                ans %= MOD
                i += 1
            else: # 縦 - 縦
                ans *= 2
                ans %= MOD
        else:
            if A[i] != B[i]:  # 横 ー 横
                ans *= 3
                ans %= MOD
                i += 1
            else: # 横 ー 縦
                pass
                # ans *= 1
                # ans %= MOD
        i += 1
    print(ans % MOD)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [next(tokens) for _ in range(2)]  # type: "List[str]"
    solve(N, S)

if __name__ == '__main__':
    main()
