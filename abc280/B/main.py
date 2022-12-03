#!/usr/bin/env python3
import sys


def solve(N: int, S: "List[int]"):
    ans = [S[0]]
    for i in range(1, N):
        ans.append(S[i] - S[i - 1])
    print(*ans)
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    S = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, S)

if __name__ == '__main__':
    main()