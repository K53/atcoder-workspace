#!/usr/bin/env python3
import sys


def solve(N: int, X: int, Y: int, A: "List[int]"):
    l = []
    tmp = []
    for aa in A:
        if aa > X or aa < Y:
            l.append(tmp)
            tmp = []
        else:
            tmp.append(aa)
    l.append(tmp)
    ans = 0
    for ll in l:
        w = []
        for i in range(len(ll)):
            if ll[i] == X:
                w.append((i, 1))
            if ll[i] == Y:
                w.append((i, -1))
        last = 0
        for i in range(len(w) - 1):
            if w[i][1] == w[i + 1][1]:
                continue
            ans += (w[i][0] - last + 1) * (len(ll) - w[i + 1][0])
            last = w[i][0] + 1
    print(ans)

    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    Y = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, Y, A)

if __name__ == '__main__':
    main()
