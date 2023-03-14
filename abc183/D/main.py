#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, W: int, S: "List[int]", T: "List[int]", P: "List[int]"):
    maxST = 2 * 10 ** 5 + 1
    imos = [0] * (maxST + 1)
    for i in range(N):
        imos[S[i]] += P[i]
        imos[T[i]] -= P[i]

    # ビルド
    for i in range(1, len(imos)):
        imos[i] += imos[i - 1]

    for num in imos:
        if num > W:
            print(NO)
            return
    print(YES)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    S = [int()] * (N)  # type: "List[int]"
    T = [int()] * (N)  # type: "List[int]"
    P = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = int(next(tokens))
        T[i] = int(next(tokens))
        P[i] = int(next(tokens))
    solve(N, W, S, T, P)

if __name__ == '__main__':
    main()
