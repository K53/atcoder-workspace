#!/usr/bin/env python3
import sys


def solve(N: int, X: int, A: "List[int]"):
    l = [0] * N
    l[X - 1] = 1
    now = X - 1
    while True:
        next = A[now] - 1
        if l[next] == 0:
            l[next] = 1
            now = next
        else:
            break
    print(sum(l))
    return


# Generated by 2.9.0 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    X = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, X, A)

if __name__ == '__main__':
    main()