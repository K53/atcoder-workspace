#!/usr/bin/env python3
import sys


def solve(N: int, A: "List[int]"):
    is_called = [0] * N
    for i in range(N):
        if is_called[i]:
            continue
        is_called[A[i] - 1] = 1
    ans = []
    for i in range(N):
        if is_called[i]:
            continue
        ans.append(i + 1)
    ans.sort()
    print(len(ans))
    print(*ans, sep=" ")
    return


# Generated by 2.12.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, A)

if __name__ == '__main__':
    main()
