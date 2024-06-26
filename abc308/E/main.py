#!/usr/bin/env python3
import sys
from collections import defaultdict

def solve(N: int, A: "List[int]", S: str):
    def mex(a, b, c):
        s = set([a, b, c])
        for i in range(4):
            if i not in s:
                return i
    d = {
        "M": {
            0: [0],
            1: [0],
            2: [0],
        },
        "E": {
            0: [0],
            1: [0],
            2: [0],
        },
        "X": {
            0: [0],
            1: [0],
            2: [0],
        },
    }
    ans = 0
    es = []
    for i in range(N):
        for ch in "MEX":
            for num in range(3):
                if ch == S[i] and num == A[i]:
                    d[ch][num].append(d[ch][num][-1] + 1)
                else:
                    d[ch][num].append(d[ch][num][-1])
        if S[i] == "E":
            es.append(i)
    for i in es:
        num = A[i]
        for mm in range(3):
            for xx in range(3):
                ans += d["M"][mm][i] * (d["X"][xx][-1] - d["X"][xx][i]) * mex(mm, num, xx)

    # for ch in "MEX":
    #     for num in range(3):
    #         print(d[ch][num])
    print(ans)
    return


# Generated by 2.13.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    S = next(tokens)  # type: str
    solve(N, A, S)

if __name__ == '__main__':
    main()
