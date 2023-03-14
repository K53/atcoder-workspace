#!/usr/bin/env python3
import sys

YES = "Yes"  # type: str
NO = "No"  # type: str

def solve(N: int, x: "List[int]", y: "List[int]"):
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                x1, y1 = x[i], y[i]
                x2, y2 = x[j], y[j]
                x3, y3 = x[k], y[k]
                if (y1 - y2) * (x1 - x3) == (y1 - y3) * (x1 - x2):
                    print(YES)
                    return
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
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)

if __name__ == '__main__':
    main()
