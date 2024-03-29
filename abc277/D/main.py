#!/usr/bin/env python3
import sys
import collections

def solve(N: int, M: int, A: "List[int]"):
    S = sum(A)
    A.sort()
    cur = A[0]
    res = []
    ss = 0
    for i in range(N):
        if cur == A[i] or cur + 1 == A[i]:
            ss += A[i]
            cur = A[i]
        else:
            res.append(ss)
            ss = A[i]
            cur = A[i]
    res.append(ss)
    if len(res) == 1:
        pass
    elif A[0] == A[-1] or A[0] == (A[-1] + 1) % M:
        res[0] += res[-1]
        del res[-1]
    print(S - max(res))
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, M, A)

if __name__ == '__main__':
    main()
