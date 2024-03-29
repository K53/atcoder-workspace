#!/usr/bin/env python3
import sys


def solve(N: int, H: "List[int]"):
    curH = H[0]
    hop = 0
    ans = 0
    for i in range(1, N):
        if H[i] <= curH:
            curH = H[i]
            hop += 1
            ans = max(ans, hop)
        else:
            curH = H[i]
            hop = 0
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
    H = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, H)

if __name__ == '__main__':
    main()
