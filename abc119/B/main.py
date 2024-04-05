#!/usr/bin/env python3
import sys


def solve(N: int, x: "List[float]", u: "List[str]"):
    ans = 0.0
    for xx, uu in zip(x, u):
        if uu == "JPY":
            ans += xx
        else:
            ans += xx * 380000.0
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
    x = [float()] * (N)  # type: "List[float]"
    u = [str()] * (N)  # type: "List[str]"
    for i in range(N):
        x[i] = float(next(tokens))
        u[i] = next(tokens)
    solve(N, x, u)

if __name__ == '__main__':
    main()
