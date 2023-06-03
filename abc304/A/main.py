#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[str]", A: "List[int]"):
    m = min(A)
    idx = A.index(m)
    for ss in(S[idx:] + S[:idx]):
        print(ss)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [str()] * (N)  # type: "List[str]"
    A = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        S[i] = next(tokens)
        A[i] = int(next(tokens))
    solve(N, S, A)

if __name__ == '__main__':
    main()
