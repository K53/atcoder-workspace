#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str


def solve(N: int, t: "List[int]", x: "List[int]", y: "List[int]"):
    l = [(0, 0, 0)]
    for tt, xx, yy in zip(t, x, y):
        l.append((tt, xx, yy))
    for i in range(N):
        tt = l[i + 1][0] - l[i][0]
        xx = abs(l[i + 1][1] - l[i][1])
        yy = abs(l[i + 1][2] - l[i][2])
        if xx + yy > tt:
            print(NO)
            return
        if (xx + yy - tt) % 2 == 1:
            print(NO)
            return
    print(YES)
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    t = [int()] * (N)  # type: "List[int]"
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        t[i] = int(next(tokens))
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, t, x, y)

if __name__ == '__main__':
    main()