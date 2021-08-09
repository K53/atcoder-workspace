#!/usr/bin/env python3
import sys


def solve(N: int, S: str):
    wl = [0]
    el = [0]
    for i in S:
        if i == "W":
            wl.append(wl[-1] + 1)
        else:
            wl.append(wl[-1])
    for i in S[::-1]:
        if i == "E":
            el.append(el[-1] + 1)
        else:
            el.append(el[-1])
    ans = 10 ** 16
    for ww, ee in zip(wl[:-1], el[:-1][::-1]):
        ans = min(ans, ww + ee)
    print(ans)
    return


# Generated by 2.6.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = next(tokens)  # type: str
    solve(N, S)

if __name__ == '__main__':
    main()
