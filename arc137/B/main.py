#!/usr/bin/env python3
import sys

def solve(N: int, A: "List[int]"):
    if N == 0:
        print(0)
        return
    S = [0]
    SS = [0]
    for aa in A:
        S.append(S[-1] + (1 if aa == 0 else -1))
    # print(S)
    minS = 0
    ansS = 0
    for i in range(N + 1):
        if minS < S[i]:
            ansS = max(S[i] - minS, ansS)
        else:
            minS = S[i]
    # print(ansS)
    for aa in reversed(A):
        SS.append(SS[-1] + (-1 if aa == 0 else 1))
    # print(SS)
    # print(max(SS))
    # print(max(S) + max(SS) + 1)
    minSS = 0
    ansSS = 0
    for i in range(N + 1):
        if minSS < SS[i]:
            ansSS = max(SS[i] - minSS, ansSS)
        else:
            minSS = SS[i]
    # print(ansSS)
    print(ansS + ansSS + 1)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
