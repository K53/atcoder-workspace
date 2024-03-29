#!/usr/bin/env python3
from collections import defaultdict
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, X: "List[int]", Y: "List[int]", S: str):
    compressedY = {val : index for index, val in enumerate(sorted(list(set(Y))))}
    # print(compressedY)
    d = defaultdict(list)
    for i in range(N):
        d[compressedY[Y[i]]].append((X[i], S[i]))
    for i, dd in d.items():
        dd.sort(key = lambda x: x[0])
        for k in range(len(dd) - 1):
            if dd[k][1] == "R" and dd[k + 1][1] == "L":
                print(YES)
                return
        # l = "".join([k[1] for k in dd])
    print(NO)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = [int()] * (N)  # type: "List[int]"
    Y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    S = next(tokens)  # type: str
    solve(N, X, Y, S)

if __name__ == '__main__':
    main()
