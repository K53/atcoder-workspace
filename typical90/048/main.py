#!/usr/bin/env python3
import sys


def solve(N: int, K: int, A: "List[int]", B: "List[int]"):
    l = []
    for i in range(N):
        l.append(A[i] - B[i])
    l.extend(B)
    l.sort(reverse=True)
    print(sum(l[:K]))
    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    K = int(next(tokens))  # type: int
    A = [int()] * (N)  # type: "List[int]"
    B = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    solve(N, K, A, B)

if __name__ == '__main__':
    main()
