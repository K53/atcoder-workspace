#!/usr/bin/env python3
import sys


def solve(N: int, Q: int, A: "List[int]", K: "List[int]"):
    import bisect
    l = [aa - i - 1 for i, aa in enumerate(A)]
    for i in range(Q):
        p = bisect.bisect_left(l, K[i])
        # print(p)
        if p == 0:
            print(K[i])
        else:
            print(K[i] - l[p - 1] + A[p - 1])

    # print(l)
        


    return


# Generated by 2.3.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    Q = int(next(tokens))  # type: int
    A = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    K = [int(next(tokens)) for _ in range(Q)]  # type: "List[int]"
    solve(N, Q, A, K)

if __name__ == '__main__':
    main()
