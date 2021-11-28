#!/usr/bin/env python3
import sys


def solve(N: int, W: "List[str]"):
    s = set()
    pre = W[0][0]
    for i in range(N):
        if W[i] in s or pre != W[i][0]:
            print("LOSE" if i % 2 == 0 else "WIN")
            return
        s.add(W[i])
        pre = W[i][-1]
    print("DRAW")
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    W = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, W)

if __name__ == '__main__':
    main()
